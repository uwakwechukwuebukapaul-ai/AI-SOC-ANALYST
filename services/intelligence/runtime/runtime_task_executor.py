"""
Sentinel DNA Runtime Task Executor

Enterprise task execution engine.

Responsibilities:

- execute runtime tasks
- manage task lifecycle
- track execution results
- handle failures
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .task import (
    Task,
    TaskStatus,
)


@dataclass
class RuntimeTaskExecutor:
    """
    Runtime task execution engine.
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
        Register task capability handler.
        """

        self.handlers[capability] = handler



    def execute(
        self,
        task: Task,
    ) -> Any:
        """
        Execute runtime task.
        """

        handler = self.handlers.get(
            task.capability
        )


        if handler is None:
            task.fail()

            self.failed += 1

            return None


        try:

            task.start()


            result = handler(
                task.payload
            )


            task.complete()


            self.executed += 1


            return result


        except Exception:

            task.fail()

            self.failed += 1

            return None



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability handler.
        """

        return capability in self.handlers



    def clear(self) -> None:
        """
        Reset executor.
        """

        self.handlers.clear()

        self.executed = 0

        self.failed = 0



    def status(self) -> dict[str, Any]:
        """
        Executor status.
        """

        return {
            "executed":
                self.executed,

            "failed":
                self.failed,

            "handlers":
                len(self.handlers),
        }