"""
Sentinel DNA Runtime Orchestrator

Central coordination layer for the Intelligence Runtime Framework.

Responsible for:
- Runtime lifecycle management
- Worker coordination
- Task submission
- Workflow execution coordination
- Runtime state reporting
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_engine import RuntimeEngine
from .worker import RuntimeWorker
from .task import Task
from .execution_result import ExecutionResult


@dataclass
class RuntimeOrchestrator:
    """
    Enterprise runtime coordination service.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    workers: dict[str, RuntimeWorker] = field(
        default_factory=dict
    )

    running: bool = False


    def start(self) -> None:
        """
        Start runtime orchestration.
        """

        self.running = True

        for worker in self.workers.values():
            worker.start()



    def stop(self) -> None:
        """
        Stop runtime orchestration.
        """

        self.running = False

        for worker in self.workers.values():
            worker.stop()



    def register_worker(
        self,
        worker_id: str,
        worker: RuntimeWorker,
    ) -> None:
        """
        Register execution worker.
        """

        self.workers[worker_id] = worker



    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task into runtime.
        """

        self.engine.submit(task)



    def execute(
        self,
        task: Task,
        handler: Callable,
    ) -> ExecutionResult:
        """
        Execute task through runtime engine.
        """

        return self.engine.execute(
            task,
            handler,
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime status snapshot.
        """

        return {
            "running": self.running,
            "workers": len(self.workers),
            "engine": self.engine.status(),
        }