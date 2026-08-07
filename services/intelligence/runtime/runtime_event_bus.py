"""
Sentinel DNA Runtime Event Bus

Enterprise internal event communication layer.

Responsibilities:

- event publishing
- subscriber registration
- event dispatching
- event history tracking
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable
from datetime import datetime, timezone


@dataclass
class RuntimeEventBus:
    """
    Runtime event dispatcher.
    """

    subscribers: dict[str, list[Callable]] = field(
        default_factory=dict
    )

    history: list[dict[str, Any]] = field(
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
    ) -> int:
        """
        Publish runtime event.
        """

        event = {
            "type":
                event_type,

            "payload":
                payload,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),
        }


        self.history.append(
            event
        )


        delivered = 0


        for handler in self.subscribers.get(
            event_type,
            [],
        ):
            handler(
                payload
            )

            delivered += 1


        return delivered



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
        Clear events.
        """

        self.subscribers.clear()

        self.history.clear()



    def status(self) -> dict[str, Any]:
        """
        Event bus status.
        """

        return {
            "events":
                len(
                    self.history
                ),

            "event_types":
                list(
                    self.subscribers.keys()
                ),
        }