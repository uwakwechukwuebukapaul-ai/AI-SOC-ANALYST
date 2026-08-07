"""
Sentinel DNA Runtime Pipeline

Enterprise execution pipeline coordinator.

Connects:
Task
 ↓
Dispatcher
 ↓
Execution
 ↓
Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .task import Task
from .execution_result import ExecutionResult
from .runtime_dispatcher import RuntimeDispatcher


@dataclass
class RuntimePipeline:
    """
    Runtime execution pipeline.

    Responsibilities:
    - task submission
    - capability routing
    - execution tracking
    - pipeline state reporting
    """

    dispatcher: RuntimeDispatcher = field(
        default_factory=RuntimeDispatcher
    )

    submitted_tasks: list[Task] = field(
        default_factory=list
    )


    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Add task to pipeline.
        """

        self.submitted_tasks.append(
            task
        )



    def register_handler(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register execution capability.
        """

        self.dispatcher.register_handler(
            capability,
            handler,
        )



    def execute(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Execute pipeline task.
        """

        return self.dispatcher.dispatch(
            task
        )



    def size(self) -> int:
        """
        Number of submitted tasks.
        """

        return len(
            self.submitted_tasks
        )



    def clear(self) -> None:
        """
        Clear pipeline queue.
        """

        self.submitted_tasks.clear()



    def status(self) -> dict[str, Any]:
        """
        Pipeline state.
        """

        return {
            "tasks":
                self.size(),

            "dispatcher":
                self.dispatcher.status(),
        }