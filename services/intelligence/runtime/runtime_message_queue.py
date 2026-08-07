"""
Sentinel DNA Runtime Message Queue

Enterprise asynchronous messaging layer.

Responsibilities:

- enqueue runtime messages
- consume messages
- track queue operations
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any



@dataclass
class RuntimeMessageQueue:
    """
    Runtime message broker.
    """

    queue: list[dict[str, Any]] = field(
        default_factory=list
    )

    processed: int = 0



    def publish(
        self,
        topic: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Add message to queue.
        """

        self.queue.append(
            {
                "topic":
                    topic,

                "payload":
                    payload,
            }
        )



    def consume(
        self,
    ) -> dict[str, Any] | None:
        """
        Consume next message.
        """

        if not self.queue:
            return None


        message = self.queue.pop(
            0
        )

        self.processed += 1


        return message



    def size(self) -> int:
        """
        Return queue size.
        """

        return len(
            self.queue
        )



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



    def status(self) -> dict[str, Any]:
        """
        Queue status.
        """

        return {
            "queue_size":
                self.size(),

            "processed":
                self.processed,
        }