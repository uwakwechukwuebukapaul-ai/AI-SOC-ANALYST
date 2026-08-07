"""
Sentinel DNA Runtime Audit Logger

Enterprise audit trail layer.

Responsibilities:

- record runtime actions
- store audit events
- provide audit history
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeAuditLogger:
    """
    Runtime audit event logger.
    """

    events: list[dict[str, Any]] = field(
        default_factory=list
    )


    def log(
        self,
        action: str,
        actor: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Record audit event.
        """

        self.events.append(
            {
                "action":
                    action,

                "actor":
                    actor,

                "details":
                    details or {},

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
            }
        )



    def count(self) -> int:
        """
        Return audit event count.
        """

        return len(
            self.events
        )



    def latest(self) -> dict[str, Any] | None:
        """
        Return latest audit event.
        """

        if not self.events:
            return None

        return self.events[-1]



    def clear(self) -> None:
        """
        Clear audit history.
        """

        self.events.clear()



    def status(self) -> dict[str, Any]:
        """
        Audit status.
        """

        return {
            "events":
                self.count(),
        }