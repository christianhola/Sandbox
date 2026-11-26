"""Small immutable contracts for the local orchestration experiment."""
from dataclasses import dataclass
from enum import Enum
import math
from typing import Awaitable, Callable, Mapping


class Status(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    BLOCKED = "blocked"


class RetryableError(Exception):
    """Transient failure in a trusted, side-effect-free worker."""


@dataclass(frozen=True)
class Task:
    id: str
    worker: str
    depends_on: tuple[str, ...] = ()
    max_attempts: int = 2
    timeout_seconds: float = 5.0
    requires_evidence: bool = False

    def __post_init__(self):
        if not self.id.strip() or not self.worker.strip():
            raise ValueError("task id and worker must not be empty")
        if type(self.max_attempts) is not int or not 1 <= self.max_attempts <= 5:
            raise ValueError("max_attempts must be between 1 and 5")
        if not math.isfinite(self.timeout_seconds) or self.timeout_seconds <= 0:
            raise ValueError("timeout must be finite and positive")
        if len(set(self.depends_on)) != len(self.depends_on):
            raise ValueError("duplicate dependency")


@dataclass(frozen=True)
class Result:
    artifact: str
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class Outcome:
    status: Status
    attempts: int
    result: Result | None = None
    reason: str | None = None


@dataclass(frozen=True)
class Event:
    task_id: str
    state: str
    attempt: int = 0


Worker = Callable[[Task, Mapping[str, Result]], Awaitable[Result]]
Verifier = Callable[[Task, Result], Awaitable[bool]]
