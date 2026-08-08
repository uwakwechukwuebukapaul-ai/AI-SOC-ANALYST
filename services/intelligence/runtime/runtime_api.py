"""
Sentinel DNA Runtime API

Service interface for controlling
the Intelligence Runtime Framework.

The RuntimeAPI owns the canonical RuntimeEngine
for the API instance and injects that engine into
the RuntimeWorker.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .health_monitor import RuntimeHealthMonitor
from .runtime_engine import RuntimeEngine
from .task import Task
from .worker import RuntimeWorker


@dataclass
class RuntimeAPI:
    """
    Runtime service gateway.

    Provides controlled access to:

    - task submission
    - task execution
    - worker lifecycle
    - runtime health
    - shared runtime state

    RuntimeEngine is the canonical execution state for
    this API instance. RuntimeWorker receives the same
    engine through dependency injection.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    worker: RuntimeWorker | None = None

    health: RuntimeHealthMonitor = field(
        default_factory=RuntimeHealthMonitor
    )

    def __post_init__(self) -> None:
        """
        Ensure the worker uses the API's canonical engine.

        If no worker was supplied, create one using the
        existing engine.

        If a worker was supplied with a different engine,
        replace its engine so the RuntimeAPI maintains one
        canonical runtime execution state.
        """

        if self.worker is None:
            self.worker = RuntimeWorker(
                engine=self.engine
            )
            return

        self.worker.engine = self.engine

    # ------------------------------------------------------------------
    # Task submission
    # ------------------------------------------------------------------

    def submit_task(
        self,
        task: Task,
    ) -> dict[str, Any]:
        """
        Submit a runtime task.

        The task is placed into the canonical RuntimeEngine
        queue and scheduler.
        """

        if not isinstance(task, Task):
            raise TypeError(
                "task must be a Task instance."
            )

        self.engine.submit(task)

        return {
            "submitted": True,
            "task_id": task.task_id,
        }

    # ------------------------------------------------------------------
    # Task execution
    # ------------------------------------------------------------------

    def execute(
        self,
        task: Task,
        handler: Callable[
            [Task, Any],
            Any,
        ],
    ):
        """
        Execute a task through the shared RuntimeWorker.
        """

        if self.worker is None:
            raise RuntimeError(
                "Runtime worker is not initialized."
            )

        return self.worker.execute_task(
            task,
            handler,
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def start(self) -> None:
        """
        Start the runtime worker and record a health heartbeat.
        """

        if self.worker is None:
            raise RuntimeError(
                "Runtime worker is not initialized."
            )

        self.worker.start()

        self.health.heartbeat()

    def stop(self) -> None:
        """
        Stop the runtime worker.
        """

        if self.worker is None:
            return

        self.worker.stop()

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return complete runtime status.
        """

        if self.worker is None:
            worker_status = {
                "running": False,
                "executed_tasks": 0,
                "failed_tasks": 0,
            }
        else:
            worker_status = self.worker.status()

        return {
            "worker": worker_status,
            "health": self.health.status(),
            "runtime": self.engine.status(),
        }