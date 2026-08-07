"""
Sentinel DNA Runtime Audit Layer

Tracks runtime events and execution history.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditEntry:
    event: str
    data: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "event": self.event,
            "data": self.data,
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class RuntimeAudit:
    """
    Runtime execution audit storage.
    """

    entries: list[AuditEntry] = field(
        default_factory=list
    )

    def record(
        self,
        event: str,
        data: dict[str, Any] | None = None,
    ) -> AuditEntry:
        entry = AuditEntry(
            event=event,
            data=data or {},
        )

        self.entries.append(entry)

        return entry


    def latest(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:

        return [
            entry.to_dict()
            for entry in self.entries[-limit:]
        ]


    def clear(self) -> None:
        self.entries.clear()


    def count(self) -> int:
        return len(self.entries)


    def to_dict(self) -> dict[str, Any]:

        return {
            "count": self.count(),
            "entries": [
                entry.to_dict()
                for entry in self.entries
            ],
        }