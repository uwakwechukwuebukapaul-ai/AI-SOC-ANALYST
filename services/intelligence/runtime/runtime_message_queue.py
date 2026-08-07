"""
Sentinel DNA Runtime Message Queue

Enterprise runtime message buffering layer.

Responsibilities:

- queue runtime messages
- publish runtime events
- consume pending messages
- track processed count
- expose queue status
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

    processed: int = 0


    def enqueue(
        self,
        message: dict[str, Any],
    ) -> None:
        """
        Add message.
        """

        self.queue.append(
            message
        )


    def publish(
        self,
        topic: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Publish message.

        Example:

        publish(
            "incident",
            {
                "id": "INC001"
            }
        )
        """

        self.enqueue(
            {
                "topic": topic,
                "payload": payload,
            }
        )


    def dequeue(self):
        """
        Remove next message.
        """

        if not self.queue:
            return None

        return self.queue.pop(
            0
        )


    def consume(self):
        """
        Consume message and track processing.
        """

        message = self.dequeue()

        if message is not None:
            self.processed += 1

        return message


    def push(
        self,
        message: dict[str, Any],
    ) -> None:
        """
        Compatibility alias.
        """

        self.enqueue(
            message
        )


    def pop(self):
        """
        Compatibility alias.
        """

        return self.dequeue()


    def mark_processed(self) -> None:
        """
        Increment processed count.
        """

        self.processed += 1


    def count(self) -> int:
        """
        Return processed messages.
        """

        return self.processed


    def clear(self) -> None:
        """
        Reset queue.
        """

        self.queue.clear()

        self.processed = 0


    def size(self) -> int:
        """
        Pending queue size.
        """

        return len(
            self.queue
        )


    def status(self) -> dict[str, Any]:
        """
        Queue status.
        """

        return {
            "queue_size": len(self.queue),
            "queued": len(self.queue),
            "processed": self.processed,
        }