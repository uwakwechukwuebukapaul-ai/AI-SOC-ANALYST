"""
Sentinel DNA Runtime Intelligence Runtime

Top-level intelligence runtime container.

Responsibilities:

- bootstrap intelligence stack
- manage runtime lifecycle
- expose intelligence interface
- provide health status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_facade import (
    RuntimeIntelligenceFacade,
)


@dataclass
class RuntimeIntelligenceRuntime:
    """
    Intelligence runtime container.
    """

    facade: RuntimeIntelligenceFacade = field(
        default_factory=RuntimeIntelligenceFacade
    )

    running: bool = False


    def start(self) -> None:
        """
        Start intelligence runtime.
        """

        self.running = True



    def stop(self) -> None:
        """
        Stop intelligence runtime.
        """

        self.running = False



    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register intelligence capability.
        """

        self.facade.register_capability(
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
        Execute intelligence request.
        """

        return self.facade.execute(
            capability,
            investigation_id,
            metadata,
        )



    def health(self) -> dict[str, Any]:
        """
        Runtime health status.
        """

        return {
            "running":
                self.running,

            "intelligence":
                self.facade.status(),
        }