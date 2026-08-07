"""
Sentinel DNA Runtime Pipeline

Enterprise runtime processing pipeline.

Responsibilities:

- accept runtime tasks
- process queued work
- dispatch capabilities
- track execution results
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_message_queue import RuntimeMessageQueue
from .runtime_dispatcher import RuntimeDispatcher


@dataclass
class RuntimePipeline:
    """
    Runtime execution pipeline.
    """

    queue: RuntimeMessageQueue = field(
        default_factory=RuntimeMessageQueue
    )

    dispatcher: RuntimeDispatcher = field(
        default_factory=RuntimeDispatcher
    )

    processed: int = 0


    def register_handler(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register execution capability.
        """

        self.dispatcher.register(
            capability,
            handler,
        )



    def submit(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Submit runtime task.
        """

        self.queue.enqueue(
            {
                "capability":
                    capability,

                "payload":
                    payload,
            }
        )



    def process(self) -> Any:
        """
        Process next queued task.
        """

        message = self.queue.dequeue()


        if message is None:
            return None


        result = self.dispatcher.dispatch(
            message["capability"],
            message["payload"],
        )


        self.processed += 1


        return result



    def size(self) -> int:
        """
        Queue size.
        """

        return self.queue.size()



    def clear(self) -> None:
        """
        Reset pipeline.
        """

        self.queue.clear()

        self.processed = 0



    def status(self) -> dict[str, Any]:
        """
        Pipeline status.
        """

        return {
            "queued":
                self.queue.size(),

            "processed":
                self.processed,

            "handlers":
                len(
                    self.dispatcher.handlers
                ),
        }