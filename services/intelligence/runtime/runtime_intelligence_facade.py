"""
Sentinel DNA Runtime Intelligence Facade

Unified intelligence access interface.

Responsibilities:

- simplify intelligence execution
- expose stable runtime interface
- coordinate controller operations
- provide enterprise abstraction layer
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_controller import (
    RuntimeIntelligenceController,
)


@dataclass
class RuntimeIntelligenceFacade:
    """
    Unified runtime intelligence interface.
    """

    controller: RuntimeIntelligenceController = field(
        default_factory=RuntimeIntelligenceController
    )


    def register_capability(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.controller.register(
            capability,
            handler,
        )


    def execute(
        self,
        capability: str,
        investigation_id: str,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Execute intelligence workflow.
        """

        return self.controller.investigate(
            {
                "capability":
                    capability,

                "investigation_id":
                    investigation_id,

                "metadata":
                    metadata,
            }
        )


    def status(self) -> dict[str, Any]:
        """
        Return runtime status.
        """

        return self.controller.status()