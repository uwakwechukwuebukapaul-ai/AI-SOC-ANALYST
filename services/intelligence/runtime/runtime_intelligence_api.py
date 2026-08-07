"""
Sentinel DNA Runtime Intelligence API

Internal service API boundary.

Responsibilities:

- expose intelligence operations
- validate requests
- manage runtime intelligence access
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_service import (
    RuntimeIntelligenceService,
)

from .runtime_intelligence_context import (
    RuntimeIntelligenceContext,
)


@dataclass
class RuntimeIntelligenceAPI:
    """
    Runtime intelligence API facade.
    """

    service: RuntimeIntelligenceService = field(
        default_factory=RuntimeIntelligenceService
    )


    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.service.register_capability(
            capability,
            handler,
        )



    def execute(
        self,
        capability: str,
        investigation_id: str,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        """
        Execute intelligence request.
        """

        context = RuntimeIntelligenceContext(
            investigation_id=investigation_id,
        )

        if metadata:
            context.metadata.update(
                metadata
            )


        return self.service.investigate(
            capability,
            context,
        )



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability.
        """

        return self.service.available(
            capability
        )



    def status(self) -> dict[str, Any]:
        """
        API status.
        """

        return self.service.status()