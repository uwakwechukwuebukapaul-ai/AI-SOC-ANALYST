"""
Sentinel DNA Runtime API

Service interface for controlling
the Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any

from .runtime_engine import RuntimeEngine
from .task import Task
from .worker import RuntimeWorker
from .health_monitor import RuntimeHealthMonitor


@dataclass
class RuntimeAPI:
    """
    Runtime service gateway.

    Provides controlled access to:
    - task submission
    - execution
    - worker state
    - runtime health
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    worker: RuntimeWorker = field(
        default_factory=RuntimeWorker
    )

    health: RuntimeHealthMonitor = field(
        default_factory=RuntimeHealthMonitor
    )


    def submit_task(
        self,
        task: Task,
    ) -> dict:

        self.engine.submit(task)

        return {
            "submitted": True,
            "task_id": task.task_id,
        }


    def execute(
        self,
        task: Task,
        handler: Callable[
            [Task, Any],
            Any
        ],
    ):

        return self.worker.execute_task(
            task,
            handler,
        )


    def start(self):

        self.worker.start()

        self.health.heartbeat()


    def stop(self):

        self.worker.stop()


    def status(self) -> dict:

        return {
            "worker":
                self.worker.status(),

            "health":
                self.health.status(),

            "runtime":
                self.engine.status(),
        }