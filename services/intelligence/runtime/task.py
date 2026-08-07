"""
Sentinel DNA Runtime Task

Enterprise runtime task model used by the
Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
import uuid


class TaskStatus(str, Enum):
    """Execution lifecycle."""

    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskPriority(int, Enum):
    """Scheduling priority."""

    LOW = 10
    NORMAL = 50
    HIGH = 75
    CRITICAL = 100


@dataclass(slots=True)
class Task:
    """
    Runtime execution task.
    """

    capability: str

    payload: dict[str, Any]

    priority: TaskPriority = TaskPriority.NORMAL

    correlation_id: str | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    task_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    status: TaskStatus = TaskStatus.PENDING

    retries: int = 0

    max_retries: int = 3

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    started_at: datetime | None = None

    completed_at: datetime | None = None

    def start(self) -> None:
        self.status = TaskStatus.RUNNING
        self.started_at = datetime.now(timezone.utc)

    def complete(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now(timezone.utc)

    def fail(self) -> None:
        self.status = TaskStatus.FAILED
        self.completed_at = datetime.now(timezone.utc)

    def cancel(self) -> None:
        self.status = TaskStatus.CANCELLED
        self.completed_at = datetime.now(timezone.utc)

    def queue(self) -> None:
        self.status = TaskStatus.QUEUED

    @property
    def can_retry(self) -> bool:
        return self.retries < self.max_retries

    def increment_retry(self) -> None:
        self.retries += 1

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "capability": self.capability,
            "payload": self.payload,
            "priority": self.priority.name,
            "status": self.status.value,
            "retries": self.retries,
            "max_retries": self.max_retries,
            "correlation_id": self.correlation_id,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),
            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
        }