"""
Sentinel DNA Runtime Facade

Unified access layer for
Intelligence Runtime Framework.

Provides simplified operations for:
- task submission
- capability registration
- execution
- runtime monitoring
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task
from .execution_result import ExecutionResult
from .runtime_service import RuntimeService


@dataclass
class RuntimeFacade:
    """
    Simplified runtime interface.
    """

    service: RuntimeService = field(
        default_factory=RuntimeService
    )


    def boot(self) -> None:
        """
        Initialize runtime.
        """

        self.service.start()



    def shutdown(self) -> None:
        """
        Shutdown runtime.
        """

        self.service.stop()



    def submit(
        self,
        task: Task,
    ) -> dict[str, Any]:
        """
        Submit task.
        """

        return self.service.submit(
            task
        )



    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register capability.
        """

        self.service.register_capability(
            capability,
            handler,
        )



    def run(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Execute task.
        """

        return self.service.execute(
            task
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime snapshot.
        """

        return self.service.health()