"""
Sentinel DNA Runtime Controller

High-level control plane for the Intelligence Runtime.

Responsible for:
- Runtime lifecycle
- Task submission
- Runtime state management
- Orchestrator coordination
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .orchestrator import RuntimeOrchestrator
from .task import Task


@dataclass
class RuntimeController:
    """
    Enterprise runtime control plane.
    """

    orchestrator: RuntimeOrchestrator = field(
        default_factory=RuntimeOrchestrator
    )

    running: bool = False


    def start(self) -> None:
        """
        Start runtime.
        """

        self.running = True

        self.orchestrator.start()


    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.running = False

        self.orchestrator.stop()


    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit runtime task.
        """

        self.orchestrator.submit(task)


    def status(self) -> dict[str, Any]:
        """
        Runtime controller status.
        """

        return {
            "running": self.running,
            "orchestrator": self.orchestrator.status(),
        }