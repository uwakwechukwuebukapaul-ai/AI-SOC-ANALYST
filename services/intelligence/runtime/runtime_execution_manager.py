"""
Sentinel DNA Runtime Execution Manager

Enterprise execution control layer.

Responsibilities:

- manage task execution
- coordinate workers
- track execution metrics
- expose runtime execution status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task

from .runtime_worker_pool import (
    RuntimeWorkerPool,
)

from .runtime_metrics_collector import (
    RuntimeMetricsCollector,
)



@dataclass
class RuntimeExecutionManager:
    """
    Runtime execution coordinator.
    """

    workers: RuntimeWorkerPool = field(
        default_factory=RuntimeWorkerPool
    )

    metrics: RuntimeMetricsCollector = field(
        default_factory=RuntimeMetricsCollector
    )

    running: bool = False



    def start(
        self,
        workers: int = 1,
    ) -> None:
        """
        Start execution manager.
        """

        self.workers.start_workers(
            workers
        )

        self.running = True



    def stop(self) -> None:
        """
        Stop execution manager.
        """

        self.workers.stop_workers()

        self.running = False



    def submit(
        self,
        task: Task,
    ) -> Any:
        """
        Submit execution task.
        """

        if not self.running:
            return None


        result = self.workers.submit(
            task
        )


        if result is not None:
            self.metrics.record_execution(
                task.capability
            )

        else:
            self.metrics.record_failure(
                task.capability,
                "execution_failed",
            )


        return result



    def clear(self) -> None:
        """
        Reset manager.
        """

        self.workers.clear()

        self.metrics.clear()



    def status(self) -> dict[str, Any]:
        """
        Execution status.
        """

        return {
            "running":
                self.running,

            "workers":
                self.workers.status(),

            "metrics":
                self.metrics.status(),
        }