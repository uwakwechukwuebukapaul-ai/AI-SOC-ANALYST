"""
Sentinel DNA Runtime Intelligence Router

Enterprise intelligence routing layer.

Responsibilities:

- analyze task requirements
- select capable agents
- route intelligence execution
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)

from .task import (
    Task,
)



@dataclass
class RuntimeIntelligenceRouter:
    """
    Intelligence routing engine.
    """

    orchestrator: RuntimeAgentOrchestrator = field(
        default_factory=RuntimeAgentOrchestrator
    )

    routes: int = 0



    def register_agent(
        self,
        agent,
    ) -> None:
        """
        Register intelligence agent.
        """

        self.orchestrator.register_agent(
            agent
        )



    def route(
        self,
        task: Task,
    ) -> Any:
        """
        Route task to intelligence agent.
        """

        self.routes += 1


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

        agents = (
            self.orchestrator.manager.find_capability(
                capability
            )
        )

        return len(agents) > 0



    def clear(self) -> None:
        """
        Reset router.
        """

        self.orchestrator.clear()

        self.routes = 0



    def status(self) -> dict[str, Any]:
        """
        Router status.
        """

        return {
            "routes":
                self.routes,

            "agents":
                self.orchestrator.status(),
        }