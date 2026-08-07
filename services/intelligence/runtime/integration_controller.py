"""
Sentinel DNA Runtime Integration Controller

Central coordination bridge for runtime services.

Responsibilities:

- Connect runtime components
- Coordinate lifecycle events
- Submit tasks
- Track execution state
- Provide runtime overview
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_engine import RuntimeEngine
from .runtime_state import RuntimeState
from .event_store import RuntimeEventStore
from .audit_logger import RuntimeAuditLogger
from .policy_engine import PolicyEngine
from .task import Task
from .execution_result import ExecutionResult


@dataclass
class RuntimeIntegrationController:
    """
    Enterprise runtime integration layer.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    state: RuntimeState = field(
        default_factory=RuntimeState
    )

    events: RuntimeEventStore = field(
        default_factory=RuntimeEventStore
    )

    audit: RuntimeAuditLogger = field(
        default_factory=RuntimeAuditLogger
    )

    policies: PolicyEngine = field(
        default_factory=PolicyEngine
    )


    def start(self) -> None:
        """
        Start integrated runtime.
        """

        self.state.start()

        self.events.append(
            "runtime_started"
        )

        self.audit.log(
            "runtime_started"
        )



    def stop(self) -> None:
        """
        Stop integrated runtime.
        """

        self.state.stop()

        self.events.append(
            "runtime_stopped"
        )

        self.audit.log(
            "runtime_stopped"
        )



    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task.
        """

        self.engine.submit(
            task
        )

        self.events.append(
            "task_submitted",
            {
                "task": str(task)
            }
        )



    def execute(
        self,
        task: Task,
        handler: Callable,
    ) -> ExecutionResult:
        """
        Execute task through runtime.
        """

        result = self.engine.execute(
            task,
            handler,
        )


        if result.success:

            self.state.record_success()

            self.events.append(
                "task_success"
            )

            self.audit.log(
                "task_success"
            )

        else:

            self.state.record_failure()

            self.events.append(
                "task_failure"
            )

            self.audit.log(
                "task_failure"
            )


        return result



    def status(self) -> dict[str, Any]:
        """
        Runtime integrated status.
        """

        return {
            "state":
                self.state.to_dict(),

            "engine":
                self.engine.status(),

            "events":
                self.events.count(),

            "audit":
                self.audit.count(),
        }