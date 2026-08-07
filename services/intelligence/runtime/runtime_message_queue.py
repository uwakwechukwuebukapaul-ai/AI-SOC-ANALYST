"""
Sentinel DNA Runtime Message Queue

Enterprise runtime message buffering layer.

Responsibilities:

- enqueue messages
- dequeue messages
- queue inspection
- message lifecycle handling
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeMessageQueue:
    """
    Runtime message queue.
    """

    queue: list[dict[str, Any]] = field(
        default_factory=list
    )


    def enqueue(
        self,
        message: dict[str, Any],
    ) -> None:
        """
        Add message to queue.
        """

        self.queue.append(
            message
        )



    def dequeue(
        self,
    ) -> dict[str, Any] | None:
        """
        Remove oldest message.
        """

        if not self.queue:
            return None

        return self.queue.pop(
            0
        )



    def peek(
        self,
    ) -> dict[str, Any] | None:
        """
        View next message.
        """

        if not self.queue:
            return None

        return self.queue[0]



    def size(
        self,
    ) -> int:
        """
        Queue size.
        """

        return len(
            self.queue
        )



    def clear(
        self,
    ) -> None:
        """
        Clear queue.
        """

        self.queue.clear()



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Queue status.
        """

        return {
            "queue_size":
                self.size(),

            "empty":
                self.size() == 0,
        }