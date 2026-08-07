"""
Sentinel DNA Runtime Audit Logger

Enterprise audit tracking layer for runtime events.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditLogger:
    """
    Runtime event audit store.
    """

    events: list[dict[str, Any]] = field(
        default_factory=list
    )


    def log(
        self,
        action: str,
        details: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Record runtime event.
        """

        event = {
            "action": action,
            "details": details or {},
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        self.events.append(event)

        return event



    def get_events(self) -> list[dict[str, Any]]:
        """
        Retrieve audit events.
        """

        return self.events



    def latest(self) -> dict[str, Any] | None:
        """
        Return latest event.
        """

        if not self.events:
            return None

        return self.events[-1]



    def count(self) -> int:
        """
        Return event count.
        """

        return len(self.events)



    def clear(self) -> None:
        """
        Clear audit history.
        """

        self.events.clear()



    def to_dict(self) -> dict[str, Any]:
        """
        Export audit state.
        """

        return {
            "total_events": self.count(),
            "events": self.events,
        }