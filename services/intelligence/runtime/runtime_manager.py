"""
Sentinel DNA Runtime Manager

High level lifecycle controller for
Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any

from .runtime_engine import RuntimeEngine
from .task import Task
from .execution_result import ExecutionResult


@dataclass
class RuntimeManager:
    """
    Controls runtime lifecycle.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    running: bool = False

    def start(self) -> None:
        """
        Start runtime.
        """

        self.running = True

    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.running = False

    def restart(self) -> None:
        """
        Restart the runtime.

        Restarting explicitly transitions the runtime
        through a stopped state before starting it again.
        """

        self.stop()
        self.start()

    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task.
        """

        if not self.running:
            raise RuntimeError(
                "Runtime is not running"
            )

        self.engine.submit(task)

    def execute(
        self,
        task: Task,
        handler: Callable,
    ) -> ExecutionResult:
        """
        Execute task.
        """

        if not self.running:
            raise RuntimeError(
                "Runtime is not running"
            )

        return self.engine.execute(
            task,
            handler,
        )

    def status(self) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {
            "running": self.running,
            "engine": self.engine.status(),
        }

    def health(self) -> dict[str, Any]:
        """
        Return runtime health information.

        The health contract intentionally mirrors the
        runtime status contract at this layer. More detailed
        health indicators can be added later without changing
        the lifecycle API.
        """

        return {
            "running": self.running,
            "engine": self.engine.status(),
        }