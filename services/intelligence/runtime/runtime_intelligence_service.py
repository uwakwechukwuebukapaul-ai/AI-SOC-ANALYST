"""
Sentinel DNA Runtime Intelligence Service

Enterprise intelligence service facade.

Responsibilities:

- expose intelligence operations
- manage execution lifecycle
- coordinate pipeline usage
- provide service status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_pipeline import (
    RuntimeIntelligencePipeline,
)

from .runtime_intelligence_context import (
    RuntimeIntelligenceContext,
)


@dataclass
class RuntimeIntelligenceService:
    """
    Intelligence service facade.
    """

    pipeline: RuntimeIntelligencePipeline = field(
        default_factory=RuntimeIntelligencePipeline
    )

    requests: int = 0


    def register_capability(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.pipeline.register(
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
        """

        result = self.pipeline.execute(
            capability,
            context,
        )

        if result is not None:
            self.requests += 1

        return result


    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        return self.pipeline.available(
            capability
        )


    def clear(self) -> None:
        """
        Reset service.
        """

        self.pipeline.clear()

        self.requests = 0


    def status(self) -> dict[str, Any]:
        """
        Service status.
        """

        return {
            "requests":
                self.requests,

            "pipeline":
                self.pipeline.status(),
        }