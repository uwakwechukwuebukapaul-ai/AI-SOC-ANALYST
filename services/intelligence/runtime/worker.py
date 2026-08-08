"""
Sentinel DNA Runtime Worker

Background execution worker responsible for
consuming scheduled tasks and executing them
through the Intelligence Runtime Engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .execution_result import ExecutionResult
from .runtime_engine import RuntimeEngine
from .task import Task


@dataclass
class RuntimeWorker:
    """
    Runtime task execution worker.

    Responsibilities:

    - worker lifecycle
    - pulling scheduled tasks
    - executing handlers
    - tracking worker state
    - supporting dependency injection of RuntimeEngine

    The engine may be injected by RuntimeAPI so the API and
    worker operate against the same runtime state.

    When no engine is supplied, a standalone RuntimeEngine
    is created automatically.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    running: bool = False

    executed_tasks: int = 0

    failed_tasks: int = 0

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def execute_task(
        self,
        task: Task,
        handler: Callable[
            [Task, Any],
            Any,
        ],
    ) -> ExecutionResult:
        """
        Execute a single runtime task.

        The worker delegates execution to its configured
        RuntimeEngine.
        """

        if not isinstance(task, Task):
            raise TypeError(
                "task must be a Task instance."
            )

        if not callable(handler):
            raise TypeError(
                "handler must be callable."
            )

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
            Any,
        ],
    ) -> ExecutionResult | None:
        """
        Execute the next scheduled task.

        This method intentionally performs one controlled
        execution cycle and is suitable for:

        - testing
        - synchronous execution
        - development workers
        - future scheduler integration
        """

        if not self.running:
            return None

        if not callable(handler):
            raise TypeError(
                "handler must be callable."
            )

        task = self.engine.next_task()

        if task is None:
            return None

        return self.execute_task(
            task,
            handler,
        )

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return worker runtime state.
        """

        return {
            "running": self.running,
            "executed_tasks": self.executed_tasks,
            "failed_tasks": self.failed_tasks,
            "engine": self.engine.status(),
        }