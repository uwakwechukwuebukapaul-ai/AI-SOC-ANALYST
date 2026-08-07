"""
Sentinel DNA Runtime Execution Gateway

Enterprise secure execution boundary.

Responsibilities:

- authorize runtime actions
- execute approved tasks
- record audit events
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_access_controller import (
    RuntimeAccessController,
)

from .runtime_execution_manager import (
    RuntimeExecutionManager,
)

from .runtime_audit_logger import (
    RuntimeAuditLogger,
)

from .task import Task



@dataclass
class RuntimeExecutionGateway:
    """
    Secure runtime execution gateway.
    """

    access: RuntimeAccessController = field(
        default_factory=RuntimeAccessController
    )

    execution: RuntimeExecutionManager = field(
        default_factory=RuntimeExecutionManager
    )

    audit: RuntimeAuditLogger = field(
        default_factory=RuntimeAuditLogger
    )


    def execute(
        self,
        actor: str,
        permission: str,
        task: Task,
    ) -> Any:
        """
        Authorize and execute task.
        """

        allowed = self.access.authorize(
            actor,
            permission,
        )


        if not allowed:

            self.audit.log(
                "execution_denied",
                actor,
                {
                    "capability":
                        task.capability,
                },
            )

            return None



        result = self.execution.submit(
            task
        )


        self.audit.log(
            "execution",
            actor,
            {
                "capability":
                    task.capability,
            },
        )


        return result



    def start(self) -> None:
        """
        Start execution engine.
        """

        self.execution.start()



    def status(self) -> dict[str, Any]:
        """
        Gateway status.
        """

        return {
            "access":
                self.access.status(),

            "execution":
                self.execution.status(),

            "audit":
                self.audit.status(),
        }