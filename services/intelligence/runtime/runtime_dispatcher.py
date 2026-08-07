"""
Sentinel DNA Runtime Dispatcher

Enterprise runtime execution router.

Responsibilities:

- register handlers
- dispatch messages
- route capabilities
- execution tracking
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeDispatcher:
    """
    Runtime message dispatcher.
    """

    handlers: dict[str, Callable] = field(
        default_factory=dict
    )

    dispatched: int = 0


    def register(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register execution handler.
        """

        self.handlers[capability] = handler



    def dispatch(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> Any:
        """
        Dispatch message.
        """

        handler = self.handlers.get(
            capability
        )

        if handler is None:
            raise ValueError(
                f"No handler registered for {capability}"
            )


        self.dispatched += 1

        return handler(
            payload
        )



    def exists(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability.
        """

        return capability in self.handlers



    def clear(self) -> None:
        """
        Clear handlers.
        """

        self.handlers.clear()

        self.dispatched = 0



    def status(self) -> dict[str, Any]:
        """
        Dispatcher status.
        """

        return {
            "handlers":
                list(
                    self.handlers.keys()
                ),

            "dispatched":
                self.dispatched,
        }