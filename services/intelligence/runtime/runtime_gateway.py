"""
Sentinel DNA Runtime Gateway

External integration boundary
for Intelligence Runtime Framework.

Responsibilities:

- expose runtime operations
- submit tasks
- execute capabilities
- provide runtime status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task
from .execution_result import ExecutionResult
from .runtime_controller import RuntimeController


@dataclass
class RuntimeGateway:
    """
    Enterprise runtime gateway.
    """

    controller: RuntimeController = field(
        default_factory=RuntimeController
    )


    def start(self) -> None:
        """
        Start runtime service.
        """

        self.controller.initialize()



    def stop(self) -> None:
        """
        Stop runtime service.
        """

        self.controller.shutdown()



    def submit(
        self,
        task: Task,
    ) -> dict[str, Any]:
        """
        Submit task request.
        """

        self.controller.submit(
            task
        )

        return {
            "submitted": True,
            "task_id": task.task_id,
        }



    def register_handler(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register execution handler.
        """

        self.controller.register(
            capability,
            handler,
        )



    def execute(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Execute runtime task.
        """

        return self.controller.execute(
            task
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime service status.
        """

        return self.controller.status()