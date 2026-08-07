"""
Sentinel DNA Runtime Event Processor

Processes runtime events and provides
event-driven execution capabilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class EventProcessor:
    """
    Runtime event processing layer.
    """

    handlers: dict[str, list[Callable]] = field(
        default_factory=dict
    )

    processed_events: int = 0

    enabled: bool = True


    def register(
        self,
        event_name: str,
        handler: Callable,
    ) -> None:
        """
        Register event handler.
        """

        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(
            handler
        )


    def process(
        self,
        event_name: str,
        payload: Any = None,
    ) -> list[Any]:
        """
        Process event.
        """

        if not self.enabled:
            return []


        results = []


        for handler in self.handlers.get(
            event_name,
            []
        ):

            results.append(
                handler(payload)
            )


        self.processed_events += 1

        return results


    def remove(
        self,
        event_name: str,
        handler: Callable,
    ) -> None:
        """
        Remove event handler.
        """

        if event_name in self.handlers:

            if handler in self.handlers[event_name]:

                self.handlers[event_name].remove(
                    handler
                )


    def clear(self) -> None:
        """
        Clear handlers.
        """

        self.handlers.clear()


    def status(self) -> dict:
        """
        Runtime status.
        """

        return {
            "events":
                list(self.handlers.keys()),

            "processed_events":
                self.processed_events,

            "enabled":
                self.enabled,
        }


    def to_dict(self) -> dict:
        """
        Export state.
        """

        return self.status()