"""
Sentinel DNA Runtime Worker Pool

Enterprise worker execution pool.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .worker import RuntimeWorker


class _DefaultExecutor:
    """
    Capability execution registry.
    """

    def __init__(self):
        self.handlers = {}


    def register(
        self,
        capability: str,
        handler,
    ) -> None:

        self.handlers[capability] = handler


    def exists(
        self,
        capability: str,
    ) -> bool:

        return capability in self.handlers


    def execute(
        self,
        task,
    ):

        handler = self.handlers.get(
            task.capability
        )

        if handler is None:
            return None

        return handler(
            task.payload
        )


    def clear(self):

        self.handlers.clear()


@dataclass
class RuntimeWorkerPool:
    """
    Runtime worker manager.
    """

    executor: Any = field(
        default_factory=_DefaultExecutor
    )

    workers: int = 0

    running: bool = False

    completed: int = 0

    _worker_instances: list = field(
        default_factory=list
    )


    def start_workers(
        self,
        count: int,
    ) -> None:

        self.running = True

        self.workers = count

        self._worker_instances = [
            RuntimeWorker()
            for _ in range(count)
        ]


    def stop_workers(self) -> None:

        self.running = False

        self.workers = 0

        self._worker_instances.clear()


    def active_workers(self) -> int:

        return self.workers


    def size(self):

        return self.workers


    def submit(
        self,
        task,
    ):

        result = self.executor.execute(
            task
        )

        if result is not None:
            self.completed += 1

        return result


    def clear(self):

        self.completed = 0

        self.workers = 0

        self._worker_instances.clear()

        self.executor.clear()


    def status(self):

        return {
            "running": self.running,
            "workers": self.workers,
            "active_workers": self.active_workers(),
            "completed": self.completed,
            "executor": self.executor,
        }