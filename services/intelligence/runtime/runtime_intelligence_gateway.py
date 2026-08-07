"""
Sentinel DNA Runtime Intelligence Gateway

Enterprise API gateway for intelligence operations.

Responsibilities:

- register intelligence agents
- check capability availability
- route intelligence requests
- expose runtime status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)


@dataclass
class RuntimeIntelligenceGateway:
    """
    Intelligence runtime gateway.
    """

    orchestrator: RuntimeAgentOrchestrator = field(
        default_factory=RuntimeAgentOrchestrator
    )

    requests: int = 0


    def register_agent(
        self,
        agent_id: str,
        capabilities: list[str],
    ) -> None:
        """
        Register intelligence agent.
        """

        self.orchestrator.register_agent(
            agent_id,
            capabilities,
        )


    def submit_request(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> str | None:
        """
        Submit intelligence request.

        Returns selected agent identity.
        """

        self.requests += 1

        return self.orchestrator.submit(
            capability,
            request,
        )


    def execute_request(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> Any:
        """
        Execute intelligence request.

        Enterprise execution path.
        """

        self.requests += 1


        task = type(
            "RuntimeTask",
            (),
            {
                "capability": capability,
                "payload": request,
            },
        )()


        return self.orchestrator.execute(
            task
        )


    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        return self.orchestrator.has_capability(
            capability
        )


    def clear(
        self,
    ) -> None:
        """
        Clear gateway state.
        """

        self.orchestrator.clear()

        self.requests = 0


    def status(
        self,
    ) -> dict[str, Any]:
        """
        Gateway status.
        """

        return {
            "requests": self.requests,

            "capabilities": {
                "available": True
            },

            "orchestrator":
                self.orchestrator.status(),
        }