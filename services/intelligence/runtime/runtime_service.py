"""
Sentinel DNA Runtime Service

Application service layer for
Intelligence Runtime Framework.

Provides:
- runtime lifecycle
- task operations
- capability registration
- execution interface
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task
from .execution_result import ExecutionResult
from .runtime_gateway import RuntimeGateway


@dataclass
class RuntimeService:
    """
    Enterprise runtime application service.
    """

    gateway: RuntimeGateway = field(
        default_factory=RuntimeGateway
    )


    active: bool = False



    def start(self) -> None:
        """
        Start runtime service.
        """

        self.gateway.start()

        self.active = True



    def stop(self) -> None:
        """
        Stop runtime service.
        """

        self.gateway.stop()

        self.active = False



    def submit(
        self,
        task: Task,
    ) -> dict[str, Any]:
        """
        Submit runtime task.
        """

        return self.gateway.submit(
            task
        )



    def register_capability(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register runtime capability.
        """

        self.gateway.register_handler(
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

        return self.gateway.execute(
            task
        )



    def health(self) -> dict[str, Any]:
        """
        Runtime health information.
        """

        return {
            "active":
                self.active,

            "runtime":
                self.gateway.status(),
        }