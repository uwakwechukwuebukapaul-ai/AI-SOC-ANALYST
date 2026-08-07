"""
Sentinel DNA Runtime Worker

Background execution worker responsible for
consuming scheduled tasks and executing them
through the Intelligence Runtime Engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any

from .task import Task
from .runtime_engine import RuntimeEngine
from .execution_result import ExecutionResult


@dataclass
class RuntimeWorker:
    """
    Runtime task execution worker.

    Responsible for:
    - worker lifecycle
    - pulling scheduled tasks
    - executing handlers
    - tracking worker state
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    running: bool = False

    executed_tasks: int = 0

    failed_tasks: int = 0


    def start(self) -> None:
        """
        Start worker lifecycle.
        """

        self.running = True


    def stop(self) -> None:
        """
        Stop worker lifecycle.
        """

        self.running = False


    def execute_task(
        self,
        task: Task,
        handler: Callable[
            [Task, Any],
            Any
        ],
    ) -> ExecutionResult:
        """
        Execute a single task.
        """

        result = self.engine.execute(
            task,
            handler,
        )

        if result.success:
            self.executed_tasks += 1
        else:
            self.failed_tasks += 1

        return result


    def run_once(
        self,
        handler: Callable[
            [Task, Any],
            Any
        ],
    ) -> ExecutionResult | None:
        """
        Execute next scheduled task.

        Used for controlled execution/testing.
        """

        if not self.running:
            return None


        task = self.engine.next_task()


        if task is None:
            return None


        return self.execute_task(
            task,
            handler,
        )


    def status(self) -> dict:
        """
        Return worker state.
        """

        return {
            "running": self.running,
            "executed_tasks": self.executed_tasks,
            "failed_tasks": self.failed_tasks,
            "engine": self.engine.status(),
        }