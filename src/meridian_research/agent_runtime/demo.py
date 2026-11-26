"""Offline demonstration; all research and artifacts are synthetic."""
import asyncio
import json
from dataclasses import asdict

from .contracts import Result, Task
from .runtime import Runtime


async def research(task, inputs):
    return Result("Synthetic API contract: id is required", ("fixture:api-contract-v1",))


async def architect(task, inputs):
    return Result("Plan: validate id before processing; " + inputs["research"].artifact)


async def verify(task, result):
    return "id" in result.artifact


async def main():
    runtime = Runtime({"research": research, "architect": architect}, verify)
    report = await runtime.run([
        Task("research", "research", requires_evidence=True),
        Task("plan", "architect", ("research",)),
    ])
    print(json.dumps({"outcomes": {k: asdict(v) for k, v in report.outcomes.items()},
                      "events": [asdict(e) for e in report.events]}, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
