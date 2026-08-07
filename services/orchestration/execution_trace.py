"""
Investigation execution trace.

Provides an auditable record of orchestration steps.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any


class ExecutionTrace:
    """Record orchestration events."""

    def __init__(self) -> None:
        self._events: list[dict[str, Any]] = []

    def record(
        self,
        *,
        step: str,
        status: str,
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Record one orchestration event."""

        event = {
            "step": step,
            "status": status,
            "details": deepcopy(details or {}),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self._events.append(event)

        return deepcopy(event)

    def all(self) -> list[dict[str, Any]]:
        """Return all recorded events."""

        return deepcopy(self._events)

    def count(self) -> int:
        """Return number of trace events."""

        return len(self._events)