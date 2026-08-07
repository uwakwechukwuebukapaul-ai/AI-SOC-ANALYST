"""
Sentinel DNA Runtime Events

Internal runtime event management layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable
import uuid


@dataclass
class RuntimeEvent:
    """
    Runtime event object.
    """

    event_type: str

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )


    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "payload": self.payload,
            "created_at": self.created_at.isoformat(),
        }



class RuntimeEventManager:
    """
    Enterprise runtime event dispatcher.
    """

    def __init__(self):

        self.events: list[RuntimeEvent] = []

        self.listeners: dict[
            str,
            list[Callable]
        ] = {}



    def publish(
        self,
        event_type: str,
        payload: dict[str, Any] | None = None,
    ) -> RuntimeEvent:
        """
        Publish runtime event.
        """

        event = RuntimeEvent(
            event_type=event_type,
            payload=payload or {},
        )

        self.events.append(event)


        for listener in self.listeners.get(
            event_type,
            [],
        ):
            listener(event)


        return event



    def subscribe(
        self,
        event_type: str,
        callback: Callable,
    ) -> None:
        """
        Subscribe listener.
        """

        if event_type not in self.listeners:
            self.listeners[event_type] = []


        self.listeners[event_type].append(
            callback
        )



    def clear(self) -> None:
        """
        Remove events.
        """

        self.events.clear()



    def count(self) -> int:
        """
        Event count.
        """

        return len(self.events)



    def to_dict(self) -> dict[str, Any]:
        """
        Export events.
        """

        return {
            "events": [
                event.to_dict()
                for event in self.events
            ],
            "count": len(self.events),
            "listeners": list(
                self.listeners.keys()
            ),
        }