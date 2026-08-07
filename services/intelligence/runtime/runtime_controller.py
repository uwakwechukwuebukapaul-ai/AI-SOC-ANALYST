"""
Sentinel DNA Runtime Controller

Enterprise runtime control plane.

Responsible for:
- runtime lifecycle
- task submission
- execution control
- health reporting
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task
from .execution_result import ExecutionResult
from .runtime_execution_manager import RuntimeExecutionManager


@dataclass
class RuntimeController:
    """
    High-level runtime controller.
    """

    manager: RuntimeExecutionManager = field(
        default_factory=RuntimeExecutionManager
    )

    initialized: bool = False


    def initialize(self) -> None:
        """
        Initialize runtime.
        """

        self.manager.start()

        self.initialized = True



    def shutdown(self) -> None:
        """
        Shutdown runtime.
        """

        self.manager.stop()

        self.initialized = False



    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit runtime task.
        """

        self.manager.submit(
            task
        )



    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register execution capability.
        """

        self.manager.register_handler(
            capability,
            handler,
        )



    def execute(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Execute task.
        """

        return self.manager.execute(
            task
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime snapshot.
        """

        return {
            "initialized":
                self.initialized,

            "runtime":
                self.manager.status(),
        }