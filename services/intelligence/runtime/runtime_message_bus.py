"""
Sentinel DNA Runtime Message Bus

Enterprise runtime communication layer.

Responsibilities:

- send runtime messages
- route messages between components
- maintain message history
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any



@dataclass
class RuntimeMessageBus:
    """
    Runtime messaging controller.
    """

    messages: list[dict[str, Any]] = field(
        default_factory=list
    )


    handlers: dict[str, list] = field(
        default_factory=dict
    )



    def register_handler(
        self,
        target: str,
        handler,
    ) -> None:
        """
        Register message receiver.
        """

        if target not in self.handlers:
            self.handlers[target] = []


        self.handlers[target].append(
            handler
        )



    def send(
        self,
        target: str,
        message: dict[str, Any],
    ) -> None:
        """
        Send runtime message.
        """

        payload = {
            "target":
                target,

            "message":
                message,
        }


        self.messages.append(
            payload
        )


        for handler in self.handlers.get(
            target,
            [],
        ):
            handler(
                message
            )



    def count(self) -> int:
        """
        Return message count.
        """

        return len(
            self.messages
        )



    def handlers_count(
        self,
        target: str,
    ) -> int:
        """
        Return handler count.
        """

        return len(
            self.handlers.get(
                target,
                [],
            )
        )



    def clear(self) -> None:
        """
        Reset message bus.
        """

        self.messages.clear()

        self.handlers.clear()



    def status(self) -> dict[str, Any]:
        """
        Message bus status.
        """

        return {
            "messages":
                self.count(),

            "targets":
                list(
                    self.handlers.keys()
                ),
        }