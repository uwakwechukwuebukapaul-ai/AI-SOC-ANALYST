"""
Sentinel DNA Runtime Event Bus

Enterprise internal event communication layer.

Responsibilities:

- publish runtime events
- subscribe handlers
- dispatch events
- manage event history
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeEventBus:
    """
    Runtime event dispatcher.
    """

    subscribers: dict[str, list[Callable]] = field(
        default_factory=dict
    )

    events: list[dict[str, Any]] = field(
        default_factory=list
    )


    def subscribe(
        self,
        event_type: str,
        handler: Callable,
    ) -> None:
        """
        Register event subscriber.
        """

        if event_type not in self.subscribers:
            self.subscribers[event_type] = []

        self.subscribers[event_type].append(
            handler
        )



    def publish(
        self,
        event_type: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Publish runtime event.
        """

        event = {
            "type": event_type,
            "payload": payload,
        }


        self.events.append(
            event
        )


        for handler in self.subscribers.get(
            event_type,
            [],
        ):
            handler(
                payload
            )



    def subscriber_count(
        self,
        event_type: str,
    ) -> int:
        """
        Return subscriber count.
        """

        return len(
            self.subscribers.get(
                event_type,
                [],
            )
        )



    def clear(self) -> None:
        """
        Reset event bus.
        """

        self.subscribers.clear()

        self.events.clear()



    def status(self) -> dict[str, Any]:
        """
        Event bus status.
        """

        return {
            "events":
                len(self.events),

            "subscriptions":
                sum(
                    len(items)
                    for items in self.subscribers.values()
                ),
        }