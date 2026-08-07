"""
Sentinel DNA Runtime Execution Manager

Enterprise execution control layer.

Responsible for:
- execution lifecycle
- pipeline coordination
- task tracking
- runtime reporting
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task
from .execution_result import ExecutionResult
from .runtime_pipeline import RuntimePipeline


@dataclass
class RuntimeExecutionManager:
    """
    Controls runtime task execution.
    """

    pipeline: RuntimePipeline = field(
        default_factory=RuntimePipeline
    )

    running: bool = False

    executed_tasks: int = 0



    def start(self) -> None:
        """
        Start execution manager.
        """

        self.running = True



    def stop(self) -> None:
        """
        Stop execution manager.
        """

        self.running = False



    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task into pipeline.
        """

        self.pipeline.submit(
            task
        )



    def register_handler(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register capability executor.
        """

        self.pipeline.register_handler(
            capability,
            handler,
        )



    def execute(
        self,
        task: Task,
    ) -> ExecutionResult:
        """
        Execute task.
        """

        result = self.pipeline.execute(
            task
        )

        self.executed_tasks += 1

        return result



    def clear(self) -> None:
        """
        Clear execution state.
        """

        self.pipeline.clear()



    def status(self) -> dict[str, Any]:
        """
        Runtime execution status.
        """

        return {
            "running":
                self.running,

            "executed_tasks":
                self.executed_tasks,

            "pipeline":
                self.pipeline.status(),
        }