"""Bounded, in-memory DAG scheduler for trusted async workers."""
import asyncio
from dataclasses import dataclass
from graphlib import TopologicalSorter
from types import MappingProxyType
from typing import Mapping, Sequence

from .contracts import Event, Outcome, Result, RetryableError, Status, Task, Verifier, Worker


@dataclass(frozen=True)
class Report:
    outcomes: Mapping[str, Outcome]
    events: tuple[Event, ...]


class Runtime:
    def __init__(self, workers: Mapping[str, Worker], verifier: Verifier, concurrency: int = 3):
        if type(concurrency) is not int or not 1 <= concurrency <= 32:
            raise ValueError("concurrency must be between 1 and 32")
        self._workers = dict(workers)
        self._verify = verifier
        self._concurrency = concurrency

    async def run(self, tasks: Sequence[Task]) -> Report:
        by_id = {task.id: task for task in tasks}
        if len(by_id) != len(tasks) or len(tasks) > 256:
            raise ValueError("duplicate task id or task limit exceeded")
        for task in tasks:
            if task.worker not in self._workers:
                raise ValueError(f"unknown worker: {task.worker}")
            if set(task.depends_on) - by_id.keys():
                raise ValueError(f"unknown dependency for {task.id}")
        graph = TopologicalSorter({t.id: t.depends_on for t in tasks})
        graph.prepare()  # Reject cycles before executing any worker.
        outcomes: dict[str, Outcome] = {}
        events: list[Event] = []
        while graph.is_active():
            ready = graph.get_ready()
            queue: asyncio.Queue[Task] = asyncio.Queue(maxsize=max(1, len(ready)))
            for task_id in ready:
                task = by_id[task_id]
                if any(outcomes[dep].status != Status.SUCCEEDED for dep in task.depends_on):
                    outcomes[task_id] = Outcome(Status.BLOCKED, 0, reason="dependency_failed")
                    events.append(Event(task_id, "blocked"))
                else:
                    queue.put_nowait(task)
                    events.append(Event(task_id, "ready"))

            async def consume():
                while not queue.empty():
                    task = queue.get_nowait()
                    try:
                        inputs = {dep: outcomes[dep].result for dep in task.depends_on}
                        outcomes[task.id] = await self._execute(task, MappingProxyType(inputs), events)
                    finally:
                        queue.task_done()

            async with asyncio.TaskGroup() as group:
                for _ in range(min(self._concurrency, queue.qsize())):
                    group.create_task(consume())
            graph.done(*ready)
        return Report(MappingProxyType(outcomes), tuple(events))

    async def _execute(self, task: Task, inputs: Mapping[str, Result], events: list[Event]) -> Outcome:
        for attempt in range(1, task.max_attempts + 1):
            events.append(Event(task.id, "running", attempt))
            try:
                async with asyncio.timeout(task.timeout_seconds):
                    result = await self._workers[task.worker](task, inputs)
                    events.append(Event(task.id, "verifying", attempt))
                    if not isinstance(result, Result) or not isinstance(result.artifact, str) or not result.artifact.strip():
                        reason = "invalid_result"
                    elif task.requires_evidence and (not result.evidence or not all(isinstance(e, str) and e.strip() for e in result.evidence)):
                        reason = "missing_evidence"
                    elif await self._verify(task, result) is not True:
                        reason = "verification_failed"
                    else:
                        events.append(Event(task.id, "succeeded", attempt))
                        return Outcome(Status.SUCCEEDED, attempt, result)
            except (RetryableError, TimeoutError) as exc:
                reason = "timeout" if isinstance(exc, TimeoutError) else "transient_error"
                if attempt < task.max_attempts:
                    events.append(Event(task.id, "retrying", attempt))
                    continue
            except Exception:
                reason = "worker_or_verifier_error"
            events.append(Event(task.id, "failed", attempt))
            return Outcome(Status.FAILED, attempt, reason=reason)
        raise AssertionError("unreachable")
