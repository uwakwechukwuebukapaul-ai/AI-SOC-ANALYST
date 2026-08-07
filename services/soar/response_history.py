"""
SOAR response history.

Records security-response actions for investigation traceability
and future enterprise audit integrations.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any


class ResponseHistory:
    """In-memory response history repository."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []

    def record(
        self,
        *,
        action: str,
        status: str,
        case_id: str | None = None,
        target: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Record a response action."""

        record = {
            "action": action,
            "status": status,
            "case_id": case_id,
            "target": target,
            "details": deepcopy(details or {}),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self._records.append(record)

        return deepcopy(record)

    def all(self) -> list[dict[str, Any]]:
        """Return all recorded response actions."""

        return deepcopy(self._records)

    def for_case(self, case_id: str) -> list[dict[str, Any]]:
        """Return response history associated with a case."""

        return [
            deepcopy(record)
            for record in self._records
            if record.get("case_id") == case_id
        ]

    def count(self) -> int:
        """Return number of recorded actions."""

        return len(self._records)