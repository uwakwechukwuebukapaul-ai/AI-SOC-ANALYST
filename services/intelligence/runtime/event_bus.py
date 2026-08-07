"""
Sentinel DNA Runtime Event Bus
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

EventHandler = Callable[[Any], None]


class EventBus:
    """
    Simple in-memory publish/subscribe event bus.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        if handler not in self._subscribers[event_name]:
            self._subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: EventHandler) -> None:
        if handler in self._subscribers[event_name]:
            self._subscribers[event_name].remove(handler)

    def publish(self, event_name: str, payload: Any = None) -> None:
        for handler in self._subscribers[event_name]:
            handler(payload)

    def subscriber_count(self, event_name: str) -> int:
        return len(self._subscribers[event_name])

    def clear(self) -> None:
        self._subscribers.clear()