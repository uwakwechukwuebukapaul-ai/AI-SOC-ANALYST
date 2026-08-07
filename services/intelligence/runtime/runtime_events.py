"""
Sentinel DNA Runtime Events

Enterprise event streaming layer.

Handles:
- event publishing
- subscriptions
- event history
- runtime communication
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable
from datetime import datetime, timezone


@dataclass
class RuntimeEvent:
    """
    Runtime event object.
    """

    name: str

    payload: Any

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )


class RuntimeEventBus:
    """
    Enterprise runtime event bus.
    """

    def __init__(self):

        self.listeners: dict[
            str,
            list[Callable]
        ] = {}

        self.history: list[
            RuntimeEvent
        ] = []



    def subscribe(
        self,
        event_name: str,
        callback: Callable,
    ) -> None:
        """
        Subscribe to event.
        """

        self.listeners.setdefault(
            event_name,
            []
        ).append(
            callback
        )



    def publish(
        self,
        event_name: str,
        payload: Any = None,
    ) -> RuntimeEvent:
        """
        Publish runtime event.
        """

        event = RuntimeEvent(
            name=event_name,
            payload=payload,
        )

        self.history.append(
            event
        )


        for callback in self.listeners.get(
            event_name,
            []
        ):
            callback(
                event
            )


        return event



    def get_history(
        self,
    ) -> list[RuntimeEvent]:
        """
        Return event history.
        """

        return self.history



    def clear(self) -> None:
        """
        Clear events.
        """

        self.history.clear()



    def status(self) -> dict:
        """
        Runtime event status.
        """

        return {
            "events":
                len(self.history),

            "subscriptions":
                sum(
                    len(x)
                    for x in self.listeners.values()
                ),
        }