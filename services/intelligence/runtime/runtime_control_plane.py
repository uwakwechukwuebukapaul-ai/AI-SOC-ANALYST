"""
Sentinel DNA Runtime Control Plane

Enterprise runtime management layer.

Responsibilities:

- runtime lifecycle
- component coordination
- execution control
- health reporting
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_execution_manager import RuntimeExecutionManager
from .runtime_security_manager import RuntimeSecurityManager
from .runtime_audit_manager import RuntimeAuditManager
from .runtime_observability_manager import RuntimeObservabilityManager
from .runtime_session_manager import RuntimeSessionManager


@dataclass
class RuntimeControlPlane:
    """
    Central runtime control service.
    """

    execution: RuntimeExecutionManager = field(
        default_factory=RuntimeExecutionManager
    )

    security: RuntimeSecurityManager = field(
        default_factory=RuntimeSecurityManager
    )

    audit: RuntimeAuditManager = field(
        default_factory=RuntimeAuditManager
    )

    observability: RuntimeObservabilityManager = field(
        default_factory=RuntimeObservabilityManager
    )

    sessions: RuntimeSessionManager = field(
        default_factory=RuntimeSessionManager
    )

    running: bool = False


    def start(self) -> None:
        """
        Start runtime control plane.
        """

        self.running = True


    def stop(self) -> None:
        """
        Stop runtime control plane.
        """

        self.running = False


    def submit(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Submit runtime execution.
        """

        self.execution.submit(
            capability,
            payload,
        )

        self.observability.increment(
            "submitted_tasks"
        )


    def execute(self) -> Any:
        """
        Execute runtime job.
        """

        result = self.execution.execute()

        self.observability.increment(
            "executed_tasks"
        )

        return result


    def status(self) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {
            "running":
                self.running,

            "execution":
                self.execution.status(),

            "security":
                self.security.status(),

            "audit":
                self.audit.status(),

            "observability":
                self.observability.status(),

            "sessions":
                self.sessions.status(),
        }