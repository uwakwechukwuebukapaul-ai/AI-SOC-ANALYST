"""
Sentinel DNA Runtime Audit Logger

Enterprise runtime audit tracking.

Responsibilities:

- Record runtime events
- Track execution history
- Provide audit search
- Export audit snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditEntry:
    """
    Runtime audit event.
    """

    event: str

    actor: str = "system"

    details: dict[str, Any] = field(
        default_factory=dict
    )

    timestamp: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )



class RuntimeAuditLogger:
    """
    Runtime audit management service.
    """

    def __init__(self):

        self.entries: list[AuditEntry] = []



    def log(
        self,
        event: str,
        actor: str = "system",
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Record audit event.
        """

        self.entries.append(
            AuditEntry(
                event=event,
                actor=actor,
                details=details or {},
            )
        )



    def count(self) -> int:
        """
        Return audit count.
        """

        return len(
            self.entries
        )



    def latest(
        self,
    ) -> AuditEntry | None:
        """
        Return latest event.
        """

        if not self.entries:
            return None

        return self.entries[-1]



    def search(
        self,
        event: str,
    ) -> list[AuditEntry]:
        """
        Search audit events.
        """

        return [
            entry
            for entry in self.entries
            if entry.event == event
        ]



    def clear(self) -> None:
        """
        Remove audit history.
        """

        self.entries.clear()



    def to_dict(self) -> list[dict[str, Any]]:
        """
        Export audit history.
        """

        return [
            {
                "event": entry.event,
                "actor": entry.actor,
                "details": entry.details,
                "timestamp":
                    entry.timestamp.isoformat(),
            }
            for entry in self.entries
        ]