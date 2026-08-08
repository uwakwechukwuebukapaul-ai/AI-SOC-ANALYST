"""
Sentinel DNA Runtime Task Executor

Executes investigation tasks through registered capability handlers.
"""

from typing import Any

from .task import (
    Task,
    TaskStatus,
)


class RuntimeTaskExecutor:
    """
    Runtime execution engine for investigation tasks.

    Responsibilities:
    - Register capability handlers
    - Execute tasks
    - Track lifecycle state
    - Record runtime metrics
    - Fail safely
    """

    def __init__(self):

        self.handlers: dict[str, Any] = {}

        self.executed = 0
        self.failed = 0
        self.completed = 0


    def register(
        self,
        capability: str,
        handler: Any,
    ) -> None:

        self.handlers[capability] = handler


    def unregister(
        self,
        capability: str,
    ) -> None:

        self.handlers.pop(
            capability,
            None,
        )


    def status(self) -> dict[str, Any]:

        return {
            "handlers": list(
                self.handlers.keys()
            ),
            "executed": self.executed,
            "completed": self.completed,
            "failed": self.failed,
        }


    def execute(
        self,
        task: Task,
    ):

        self.executed += 1

        handler = self.handlers.get(
            task.capability
        )


        if handler is None:

            task.status = TaskStatus.FAILED

            task.error = (
                f"Agent not found: {task.capability}"
            )

            self.failed += 1

            return None


        try:

            task.status = TaskStatus.RUNNING


            result = handler(
                task.payload
            )


            if result is None:

                task.status = TaskStatus.FAILED

                task.error = (
                    f"Agent execution returned no result: "
                    f"{task.capability}"
                )

                self.failed += 1

                return None


            task.status = TaskStatus.COMPLETED

            task.result = result

            self.completed += 1

            return result


        except Exception as exc:

            task.status = TaskStatus.FAILED

            task.error = str(exc)

            self.failed += 1

            return None