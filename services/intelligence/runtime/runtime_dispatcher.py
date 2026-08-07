"""
Sentinel DNA Runtime Dispatcher

Routes scheduled tasks to execution workers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .task import Task
from .execution_result import ExecutionResult
from .worker import RuntimeWorker


@dataclass
class RuntimeDispatcher:
    """
    Enterprise task dispatch layer.

    Responsible for:
    - worker registration
    - task routing
    - execution delegation
    - dispatcher state reporting
    """

    workers: dict[str, RuntimeWorker] = field(
        default_factory=dict
    )

    handlers: dict[str, Callable] = field(
        default_factory=dict
    )


    def register_worker(
        self,
        worker_id: str,
        worker: RuntimeWorker,
    ) -> None:
        """
        Register runtime worker.
        """

        self.workers[worker_id] = worker



    def register_handler(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register capability handler.
        """

        self.handlers[capability] = handler



    def dispatch(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Dispatch task based on capability.
        """

        handler = self.handlers.get(
            task.capability
        )

        if handler is None:

            return ExecutionResult.failure(
                f"No handler for capability: {task.capability}"
            )


        try:

            result = handler(
                task
            )

            return ExecutionResult.ok(
                data={
                    "result": result
                }
            )


        except Exception as exc:

            return ExecutionResult.failure(
                str(exc)
            )



    def worker_count(self) -> int:
        """
        Return registered workers.
        """

        return len(
            self.workers
        )



    def status(self) -> dict[str, Any]:
        """
        Dispatcher status.
        """

        return {
            "workers":
                self.worker_count(),

            "handlers":
                len(
                    self.handlers
                ),
        }