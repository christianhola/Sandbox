import asyncio
from graphlib import CycleError

import pytest

from meridian_research.agent_runtime.contracts import Result, RetryableError, Status, Task
from meridian_research.agent_runtime.runtime import Runtime


async def accept(task, result):
    return True


async def good(task, inputs):
    return Result(task.id, ("fixture",))


def test_dependency_verified_before_execution():
    seen = []

    async def worker(task, inputs):
        seen.append(task.id)
        if task.id == "plan":
            assert inputs["research"].artifact == "research"
        return await good(task, inputs)

    report = asyncio.run(Runtime({"w": worker}, accept).run([
        Task("plan", "w", ("research",)), Task("research", "w", requires_evidence=True)]))
    assert seen == ["research", "plan"]
    assert all(o.status == Status.SUCCEEDED for o in report.outcomes.values())
    assert [(e.task_id, e.state) for e in report.events].index(("research", "succeeded")) < [(e.task_id, e.state) for e in report.events].index(("plan", "running"))


def test_missing_evidence_blocks_descendants():
    async def worker(task, inputs):
        assert task.id == "research"
        return Result("unsubstantiated")
    report = asyncio.run(Runtime({"w": worker}, accept).run([
        Task("research", "w", requires_evidence=True), Task("plan", "w", ("research",)), Task("code", "w", ("plan",))]))
    assert report.outcomes["research"].reason == "missing_evidence"
    assert report.outcomes["plan"].status == report.outcomes["code"].status == Status.BLOCKED


def test_retries_are_bounded():
    async def worker(task, inputs):
        raise RetryableError()
    report = asyncio.run(Runtime({"w": worker}, accept).run([Task("a", "w", max_attempts=2)]))
    assert report.outcomes["a"].attempts == 2
    assert report.outcomes["a"].status == Status.FAILED
    assert sum(e.state == "retrying" for e in report.events) == 1


def test_transient_recovery():
    calls = 0
    async def worker(task, inputs):
        nonlocal calls
        calls += 1
        if calls == 1:
            raise RetryableError()
        return Result("ok")
    report = asyncio.run(Runtime({"w": worker}, accept).run([Task("a", "w")]))
    assert report.outcomes["a"].status == Status.SUCCEEDED
    assert calls == 2


def test_timeout():
    async def worker(task, inputs):
        await asyncio.sleep(1)
        return Result("late")
    report = asyncio.run(Runtime({"w": worker}, accept).run([Task("a", "w", max_attempts=1, timeout_seconds=.01)]))
    assert report.outcomes["a"].reason == "timeout"


def test_verifier_rejection():
    async def reject(task, result):
        return False
    report = asyncio.run(Runtime({"w": good}, reject).run([Task("a", "w"), Task("b", "w", ("a",))]))
    assert report.outcomes["a"].reason == "verification_failed"
    assert report.outcomes["b"].status == Status.BLOCKED


@pytest.mark.parametrize("tasks,error", [
    ([Task("a", "w", ("b",)), Task("b", "w", ("a",))], CycleError),
    ([Task("a", "w", ("missing",))], ValueError),
    ([Task("a", "w"), Task("a", "w")], ValueError),
    ([Task("a", "unknown")], ValueError),
])
def test_invalid_graph_never_executes(tasks, error):
    async def never(task, inputs):
        pytest.fail("worker executed on invalid graph")
    with pytest.raises(error):
        asyncio.run(Runtime({"w": never}, accept).run(tasks))


def test_parallelism_is_bounded():
    async def scenario():
        active = peak = 0
        release = asyncio.Event()
        async def worker(task, inputs):
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            if active == 2:
                release.set()
            await release.wait()
            await asyncio.sleep(0)
            active -= 1
            return Result(task.id)
        report = await Runtime({"w": worker}, accept, concurrency=2).run([Task(str(i), "w") for i in range(5)])
        assert peak == 2
        assert all(o.status == Status.SUCCEEDED for o in report.outcomes.values())
    asyncio.run(scenario())


def test_cancellation_reaches_worker():
    async def scenario():
        started, cleaned = asyncio.Event(), asyncio.Event()
        async def worker(task, inputs):
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                cleaned.set()
        running = asyncio.create_task(Runtime({"w": worker}, accept).run([Task("a", "w")]))
        await started.wait()
        running.cancel()
        with pytest.raises(asyncio.CancelledError):
            await running
        assert cleaned.is_set()
    asyncio.run(scenario())
