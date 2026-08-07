"""
Sentinel DNA Runtime Event Store

Enterprise runtime event persistence layer.

Responsibilities:

- Store runtime events
- Retrieve event history
- Filter events
- Provide event snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeEvent:
    """
    Runtime event record.
    """

    event_type: str

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    timestamp: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )



class RuntimeEventStore:
    """
    Runtime event storage service.
    """

    def __init__(self):

        self.events: list[RuntimeEvent] = []



    def append(
        self,
        event_type: str,
        payload: dict[str, Any] | None = None,
    ) -> RuntimeEvent:
        """
        Add event to store.
        """

        event = RuntimeEvent(
            event_type=event_type,
            payload=payload or {},
        )

        self.events.append(
            event
        )

        return event



    def all(
        self,
    ) -> list[RuntimeEvent]:
        """
        Return all events.
        """

        return self.events



    def latest(
        self,
    ) -> RuntimeEvent | None:
        """
        Return latest event.
        """

        if not self.events:
            return None

        return self.events[-1]



    def find(
        self,
        event_type: str,
    ) -> list[RuntimeEvent]:
        """
        Filter events by type.
        """

        return [
            event
            for event in self.events
            if event.event_type == event_type
        ]



    def clear(self) -> None:
        """
        Remove all events.
        """

        self.events.clear()



    def count(self) -> int:
        """
        Return number of events.
        """

        return len(
            self.events
        )



    def to_dict(self) -> list[dict[str, Any]]:
        """
        Export events.
        """

        return [
            {
                "event_type": event.event_type,
                "payload": event.payload,
                "timestamp":
                    event.timestamp.isoformat(),
            }
            for event in self.events
        ]