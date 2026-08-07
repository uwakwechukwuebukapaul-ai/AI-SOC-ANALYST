"""
Sentinel DNA Runtime Intelligence Gateway

Enterprise intelligence access layer.

Responsibilities:

- register intelligence capabilities
- execute intelligence requests
- route runtime intelligence tasks
- track requests
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_orchestrator import RuntimeAgentOrchestrator


@dataclass
class RuntimeIntelligenceGateway:
    """
    Runtime intelligence gateway.
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
        """

        agent = self.orchestrator.submit(
            capability,
            request,
        )

        if agent:
            self.requests += 1

        return agent



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        for agent in self.orchestrator.scheduler.agents.values():

            if capability in agent["capabilities"]:
                return True

        return False



    def clear(self) -> None:
        """
        Reset gateway.
        """

        self.orchestrator.clear()

        self.requests = 0



    def status(self) -> dict[str, Any]:
        """
        Gateway status.
        """

        return {
            "requests":
                self.requests,

            "orchestrator":
                self.orchestrator.status(),
        }