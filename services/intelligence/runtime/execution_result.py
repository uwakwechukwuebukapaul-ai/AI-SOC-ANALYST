"""
Sentinel DNA Runtime Execution Result

Standardized execution result returned by every
runtime intelligence component.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class ExecutionResult:
    """
    Standard execution response.
    """

    success: bool

    output: Any = None

    error: str | None = None

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)

    duration_ms: float = 0.0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @property
    def failed(self) -> bool:
        return not self.success

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.metadata[key] = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "output": self.output,
            "error": self.error,
            "confidence": self.confidence,
            "metadata": self.metadata,
            "duration_ms": self.duration_ms,
            "created_at": self.created_at.isoformat(),
        }