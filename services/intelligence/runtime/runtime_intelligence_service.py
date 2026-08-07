"""
Sentinel DNA Runtime Intelligence Service

Enterprise intelligence runtime service facade.

Responsibilities:

- expose intelligence operations API
- register intelligence capabilities
- execute investigations
- coordinate gateway/router runtime
- maintain request metrics
- expose runtime status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_intelligence_gateway import (
    RuntimeIntelligenceGateway,
)

from .runtime_intelligence_router import (
    RuntimeIntelligenceRouter,
)


@dataclass
class RuntimeIntelligenceContext:
    """
    Investigation execution context.
    """

    investigation_id: str



@dataclass
class RuntimeIntelligenceService:
    """
    Main intelligence runtime service.

    Acts as the public API layer above
    runtime routing components.
    """

    gateway: RuntimeIntelligenceGateway = field(
        default_factory=RuntimeIntelligenceGateway
    )

    router: RuntimeIntelligenceRouter = field(
        default_factory=RuntimeIntelligenceRouter
    )

    requests: int = 0


    def register_capability(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.router.register(
            capability,
            handler,
        )


    def investigate(
        self,
        capability: str,
        context: RuntimeIntelligenceContext,
    ) -> Any:
        """
        Execute intelligence investigation.

        Returns:
            execution result

        Returns None when capability
        is unavailable.
        """

        self.requests += 1


        if not self.router.available(
            capability
        ):
            return None


        return self.router.route(
            capability,
            context,
        )


    def register_agent(
        self,
        agent_id: str,
        capabilities: list[str],
    ) -> None:
        """
        Register runtime intelligence agent.
        """

        self.gateway.register_agent(
            agent_id,
            capabilities,
        )


    def submit(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> Any:
        """
        Submit runtime request.
        """

        self.requests += 1


        return self.gateway.submit_request(
            capability,
            request,
        )


    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        return self.router.available(
            capability
        )


    def clear(
        self,
    ) -> None:
        """
        Reset runtime state.
        """

        self.gateway.clear()

        self.router.clear()

        self.requests = 0



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {

            "requests": self.requests,


            "pipeline": {
                "active": True,
                "components": [
                    "gateway",
                    "router",
                    "capability_registry",
                ],
            },


            "gateway":
                self.gateway.status(),


            "router":
                self.router.status(),

        }