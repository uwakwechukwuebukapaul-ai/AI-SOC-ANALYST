"""
Sentinel DNA Runtime Execution Result

Represents the outcome of runtime task execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class ExecutionResult:
    """
    Runtime execution response.
    """

    success: bool

    message: str = ""

    data: dict[str, Any] = field(
        default_factory=dict
    )

    error: str | None = None

    execution_time: float = 0.0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    @classmethod
    def ok(
        cls,
        data: dict[str, Any] | None = None,
        message: str = "Execution completed",
    ) -> "ExecutionResult":

        return cls(
            success=True,
            message=message,
            data=data or {},
        )


    @classmethod
    def failure(
        cls,
        error: str,
        message: str = "Execution failed",
    ) -> "ExecutionResult":

        return cls(
            success=False,
            message=message,
            error=error,
        )


    def to_dict(self) -> dict[str, Any]:

        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "error": self.error,
            "execution_time": self.execution_time,
            "created_at": self.created_at.isoformat(),
        }