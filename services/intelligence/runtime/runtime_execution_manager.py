"""
Sentinel DNA Runtime Execution Manager

Enterprise runtime execution coordinator.

Responsibilities:

- runtime lifecycle management
- capability registration
- task execution
- execution tracking
- metrics reporting
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .execution_result import ExecutionResult
from .runtime_metrics_collector import (
    RuntimeMetricsCollector,
)
from .runtime_worker_pool import (
    RuntimeWorkerPool,
)
from .task import Task


@dataclass
class RuntimeExecutionManager:
    """
    Coordinates runtime execution.
    """

    workers: RuntimeWorkerPool = field(
        default_factory=RuntimeWorkerPool
    )

    metrics: RuntimeMetricsCollector = field(
        default_factory=RuntimeMetricsCollector
    )

    running: bool = False


    @property
    def pipeline(self):
        """
        Compatibility alias.

        Used by:
        RuntimeOrchestrationService tests
        """

        return self.workers


    def start(self) -> None:
        """
        Start execution runtime.
        """

        self.running = True

        if self.workers.active_workers() == 0:
            self.workers.start_workers(1)


    def stop(self) -> None:
        """
        Stop execution runtime.
        """

        self.running = False

        self.workers.stop_workers()


    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register execution capability.
        """

        self.workers.executor.register(
            capability,
            handler,
        )


    def register_handler(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Compatibility registration.
        """

        self.register(
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

        if not self.running:
            self.start()


        try:

            result = self.workers.submit(
                task
            )


            self.metrics.record_execution(
                task.capability
            )


            return ExecutionResult.ok(
                data={
                    "result": result
                }
            )


        except Exception as exc:

            capability = getattr(
                task,
                "capability",
                "unknown",
            )


            self.metrics.record_failure(
                capability
            )


            return ExecutionResult.failure(
                str(exc)
            )


    def submit(
        self,
        task,
        payload=None,
    ) -> Any:
        """
        Submit runtime task.

        Supported:

        submit(Task)

        submit(Task, payload)

        submit("capability", payload)
        """


        # legacy string capability API
        if isinstance(task, str):

            task = Task(
                capability=task,
                payload=payload or {},
            )


        elif payload is not None:

            task.payload = payload


        result = self.execute(
            task
        )


        if hasattr(result, "data"):

            return result.data.get(
                "result"
            )


        return result


    def clear(self) -> None:
        """
        Clear runtime state.
        """

        self.metrics.clear()

        self.workers.clear()



    def status(self) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {

            "running":
                self.running,


            "workers":
                self.workers.status(),


            "metrics":
                self.metrics.status(),

        }