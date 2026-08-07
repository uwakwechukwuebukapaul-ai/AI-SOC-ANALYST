"""
Sentinel DNA Runtime API Gateway

Enterprise runtime integration boundary.

Responsibilities:

- validate runtime requests
- dispatch runtime commands
- expose platform operations
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_platform_orchestrator import (
    RuntimePlatformOrchestrator,
)



@dataclass
class RuntimeAPIGateway:
    """
    Runtime command gateway.
    """

    platform: RuntimePlatformOrchestrator = field(
        default_factory=RuntimePlatformOrchestrator
    )

    handlers: dict[str, Callable] = field(
        default_factory=dict
    )


    requests: int = 0



    def register(
        self,
        command: str,
        handler: Callable,
    ) -> None:
        """
        Register API command.
        """

        self.handlers[command] = handler



    def dispatch(
        self,
        command: str,
        payload: dict[str, Any],
    ) -> Any:
        """
        Execute runtime command.
        """

        self.requests += 1


        handler = self.handlers.get(
            command
        )


        if handler is None:
            return None


        return handler(
            payload
        )



    def health(self) -> dict[str, Any]:
        """
        Gateway health.
        """

        return {
            "requests":
                self.requests,

            "platform":
                self.platform.health(),
        }



    def clear(self) -> None:
        """
        Reset gateway.
        """

        self.handlers.clear()

        self.requests = 0



    def status(self) -> dict[str, Any]:
        """
        Gateway status.
        """

        return {
            "commands":
                list(
                    self.handlers.keys()
                ),

            "requests":
                self.requests,
        }