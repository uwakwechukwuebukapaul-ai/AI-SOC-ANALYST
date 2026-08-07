"""
Sentinel DNA Runtime Gateway

Internal service gateway for Intelligence Runtime.

Responsibilities:

- Runtime access abstraction
- Task submission
- Lifecycle commands
- Runtime queries
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_controller import RuntimeController
from .task import Task
from .execution_result import ExecutionResult


@dataclass
class RuntimeGateway:
    """
    Enterprise runtime access gateway.
    """

    controller: RuntimeController = field(
        default_factory=RuntimeController
    )


    def start(self) -> None:
        """
        Start runtime.
        """

        self.controller.start()



    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.controller.stop()



    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task.
        """

        self.controller.engine.submit(
            task
        )



    def execute(
        self,
        task: Task,
        handler: Callable,
    ) -> ExecutionResult:
        """
        Execute runtime task.
        """

        return self.controller.engine.execute(
            task,
            handler,
        )



    def health(self) -> dict[str, Any]:
        """
        Runtime health.
        """

        return self.controller.health()



    def status(self) -> dict[str, Any]:
        """
        Runtime status.
        """

        return self.controller.status()