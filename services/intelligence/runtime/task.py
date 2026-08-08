"""
Sentinel DNA Runtime Task Model

Defines investigation task lifecycle state.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TaskStatus(Enum):
    """
    Runtime task lifecycle states.
    """

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"


@dataclass(slots=True)
class Task:
    """
    Runtime executable investigation task.
    """

    capability: str

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    status: TaskStatus = TaskStatus.PENDING

    result: Any = None

    error: str | None = None