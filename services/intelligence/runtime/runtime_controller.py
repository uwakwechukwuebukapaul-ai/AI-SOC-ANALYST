"""
Sentinel DNA Runtime Controller

High-level control plane for the Intelligence Runtime Framework.

Responsible for:
- Runtime startup
- Runtime shutdown
- Component coordination
- Runtime state management
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .orchestrator import RuntimeOrchestrator
from .execution_pipeline import ExecutionPipeline


@dataclass
class RuntimeController:
    """
    Runtime control plane.
    """

    orchestrator: RuntimeOrchestrator = field(
        default_factory=RuntimeOrchestrator
    )

    pipeline: ExecutionPipeline = field(
        default_factory=ExecutionPipeline
    )

    active: bool = False


    def start(self) -> None:
        """
        Start runtime system.
        """

        self.orchestrator.start()

        self.active = True



    def stop(self) -> None:
        """
        Stop runtime system.
        """

        self.orchestrator.stop()

        self.active = False



    def restart(self) -> None:
        """
        Restart runtime.
        """

        self.stop()

        self.start()



    def execute_pipeline(
        self,
        payload: Any,
    ) -> Any:
        """
        Execute payload through pipeline.
        """

        return self.pipeline.execute(
            payload
        )



    def status(self) -> dict:
        """
        Runtime controller status.
        """

        return {
            "active": self.active,
            "orchestrator":
                self.orchestrator.status(),
            "pipeline":
                self.pipeline.status(),
        }