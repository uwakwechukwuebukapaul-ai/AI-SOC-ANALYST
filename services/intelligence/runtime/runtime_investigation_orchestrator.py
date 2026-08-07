"""
Sentinel DNA Runtime Investigation Orchestrator

Enterprise investigation coordination layer.

Responsibilities:

- create investigations
- route investigation tasks
- track investigation execution
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_router import (
    RuntimeIntelligenceRouter,
)

from .task import (
    Task,
)



@dataclass
class RuntimeInvestigationOrchestrator:
    """
    Investigation workflow runtime.
    """

    router: RuntimeIntelligenceRouter = field(
        default_factory=RuntimeIntelligenceRouter
    )

    investigations: int = 0



    def register_agent(
        self,
        agent,
    ) -> None:
        """
        Register investigation agent.
        """

        self.router.register_agent(
            agent
        )



    def investigate(
        self,
        capability: str,
        evidence: dict[str, Any],
    ) -> Any:
        """
        Execute investigation.
        """

        task = Task(
            capability=capability,
            payload=evidence,
        )


        result = self.router.route(
            task
        )


        if result is not None:
            self.investigations += 1


        return result



    def count(self) -> int:
        """
        Return investigation count.
        """

        return self.investigations



    def clear(self) -> None:
        """
        Reset investigations.
        """

        self.router.clear()

        self.investigations = 0



    def status(self) -> dict[str, Any]:
        """
        Investigation runtime status.
        """

        return {
            "investigations":
                self.investigations,

            "router":
                self.router.status(),
        }