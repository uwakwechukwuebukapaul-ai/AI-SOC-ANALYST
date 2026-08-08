"""
Sentinel DNA Runtime Task Executor

Executes registered runtime capabilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .task import TaskStatus


@dataclass
class RuntimeTaskExecutor:
    """
    Runtime capability executor.
    """

    handlers: dict[str, Callable] = field(
        default_factory=dict
    )

    executed: int = 0

    failed: int = 0


    def register(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register execution handler.
        """

        self.handlers[capability] = handler


    def available(
        self,
        capability: str,
    ) -> bool:
        return capability in self.handlers


    def execute(
        self,
        task,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        """
        Execute runtime task.
        """

        if hasattr(task, "capability"):

            capability = task.capability

            task_payload = task.payload

        else:

            capability = task

            task_payload = payload or {}


        handler = self.handlers.get(
            capability
        )


        if handler is None:

            self.failed += 1

            return None


        try:

            if hasattr(task, "status"):

                task.status = TaskStatus.RUNNING


            result = handler(
                task_payload
            )


            if hasattr(task, "status"):

                task.status = TaskStatus.COMPLETED


            self.executed += 1


            return result


        except Exception as error:

            print(
                f"[RuntimeTaskExecutor ERROR] "
                f"{capability}: {error}"
            )


            if hasattr(task, "status"):

                task.status = TaskStatus.FAILED


            self.failed += 1

            raise


    def clear(self) -> None:

        self.handlers.clear()


    def status(self) -> dict[str, Any]:

        return {
            "handlers": list(
                self.handlers.keys()
            ),
            "executed": self.executed,
            "failed": self.failed,
        }