"""
Sentinel DNA Runtime Intelligence Pipeline

Enterprise intelligence processing pipeline.

Responsibilities:

- process intelligence requests
- manage context flow
- route capabilities
- track executions
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_router import RuntimeIntelligenceRouter
from .runtime_intelligence_context import RuntimeIntelligenceContext


@dataclass
class RuntimeIntelligencePipeline:
    """
    Intelligence execution pipeline.
    """

    router: RuntimeIntelligenceRouter = field(
        default_factory=RuntimeIntelligenceRouter
    )

    executions: int = 0


    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.router.register(
            capability,
            handler,
        )



    def execute(
        self,
        capability: str,
        context: RuntimeIntelligenceContext,
    ) -> Any:
        """
        Execute intelligence capability.
        """

        result = self.router.route(
            capability,
            context,
        )


        if result is not None:
            self.executions += 1


        return result



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability.
        """

        return self.router.available(
            capability
        )



    def clear(self) -> None:
        """
        Reset pipeline.
        """

        self.router.clear()

        self.executions = 0



    def status(self) -> dict[str, Any]:
        """
        Pipeline status.
        """

        return {
            "executions":
                self.executions,

            "router":
                self.router.status(),
        }