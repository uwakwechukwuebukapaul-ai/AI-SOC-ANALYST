"""
Sentinel DNA Runtime Audit Logger
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass
class RuntimeAuditLogger:
    """
    Runtime audit logger.
    """

    records: list[dict[str, Any]] = field(default_factory=list)

    def record(
        self,
        actor: str,
        action: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Record an audit event.
        """

        self.records.append(
            {
                "timestamp": datetime.now(UTC),
                "actor": actor,
                "action": action,
                "details": details or {},
            }
        )

    def log(
        self,
        action: str,
        actor: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Compatibility wrapper used by the runtime execution gateway.

        New runtime:
            log(action, actor, details)

        Legacy tests:
            record(actor, action, details)
        """

        self.record(
            actor=actor,
            action=action,
            details=details,
        )

    def latest(self) -> dict[str, Any] | None:
        """
        Return the newest audit record.
        """

        if not self.records:
            return None

        return self.records[-1]

    def count(self) -> int:
        """
        Number of audit records.
        """

        return len(self.records)

    def clear(self) -> None:
        """
        Remove all audit records.
        """

        self.records.clear()

    def status(self) -> dict[str, Any]:
        """
        Runtime audit status.
        """

        return {
            "records": self.count(),
            "latest": self.latest(),
        }