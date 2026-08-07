"""
Sentinel DNA Runtime Intelligence Router

Enterprise intelligence capability routing layer.

Responsibilities:

- register intelligence handlers
- route requests
- capability lookup
- routing metrics
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeIntelligenceRouter:
    """
    Intelligence capability router.
    """

    routes: dict[str, Callable] = field(
        default_factory=dict
    )

    routed: int = 0


    def register(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register capability handler.
        """

        self.routes[capability] = handler



    def route(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> Any:
        """
        Route intelligence request.
        """

        handler = self.routes.get(
            capability
        )


        if handler is None:
            return None


        self.routed += 1


        return handler(
            payload
        )



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability.
        """

        return capability in self.routes



    def clear(self) -> None:
        """
        Reset router.
        """

        self.routes.clear()

        self.routed = 0



    def status(self) -> dict[str, Any]:
        """
        Router status.
        """

        return {
            "capabilities":
                list(
                    self.routes.keys()
                ),

            "routed":
                self.routed,
        }