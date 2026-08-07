"""
Sentinel DNA Runtime Control Plane

Enterprise runtime operations layer.

Responsibilities:

- coordinate runtime services
- manage lifecycle
- expose operational state
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_execution_manager import (
    RuntimeExecutionManager,
)

from .runtime_event_orchestrator import (
    RuntimeEventOrchestrator,
)

from .runtime_health_monitor import (
    RuntimeHealthMonitor,
)

from .task import Task



@dataclass
class RuntimeControlPlane:
    """
    Runtime operational controller.
    """

    execution: RuntimeExecutionManager = field(
        default_factory=RuntimeExecutionManager
    )

    events: RuntimeEventOrchestrator = field(
        default_factory=RuntimeEventOrchestrator
    )

    health: RuntimeHealthMonitor = field(
        default_factory=RuntimeHealthMonitor
    )


    running: bool = False



    def start(self) -> None:
        """
        Start runtime control plane.
        """

        self.execution.start()

        self.health.runtime.start()

        self.running = True



    def stop(self) -> None:
        """
        Stop runtime control plane.
        """

        self.execution.stop()

        self.health.runtime.stop()

        self.running = False



    def submit(
        self,
        task: Task,
    ) -> Any:
        """
        Submit intelligence task.
        """

        return self.execution.submit(
            task
        )



    def emit(
        self,
        event_type: str,
        payload: dict[str, Any],
    ) -> list[Any]:
        """
        Emit runtime event.
        """

        return self.events.emit(
            event_type,
            payload,
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime operational status.
        """

        return {
            "running":
                self.running,

            "execution":
                self.execution.status(),

            "events":
                self.events.status(),

            "health":
                self.health.check(),
        }