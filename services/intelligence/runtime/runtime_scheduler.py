"""
Sentinel DNA Runtime Scheduler

Enterprise runtime scheduling layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeScheduler:
    """
    Runtime task scheduler.
    """

    tasks: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )

    def register(
        self,
        name: str,
        task: Callable[[], None],
        enabled: bool = True,
    ) -> None:
        """
        Register a scheduled task.
        """

        self.tasks[name] = {
            "task": task,
            "enabled": enabled,
        }

    def run(
        self,
        name: str,
    ) -> bool:
        """
        Execute a scheduled task.
        """

        scheduled = self.tasks.get(name)

        if scheduled is None:
            return False

        if not scheduled["enabled"]:
            return False

        scheduled["task"]()

        return True

    def enable(
        self,
        name: str,
    ) -> None:
        """
        Enable a task.
        """

        if name in self.tasks:
            self.tasks[name]["enabled"] = True

    def disable(
        self,
        name: str,
    ) -> None:
        """
        Disable a task.
        """

        if name in self.tasks:
            self.tasks[name]["enabled"] = False

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove a task.
        """

        self.tasks.pop(name, None)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check task existence.
        """

        return name in self.tasks

    def count(
        self,
    ) -> int:
        """
        Return task count.
        """

        return len(self.tasks)

    def clear(
        self,
    ) -> None:
        """
        Reset scheduler.
        """

        self.tasks.clear()

    def status(
        self,
    ) -> dict[str, Any]:
        """
        Scheduler status.
        """

        return {
            "count": self.count(),
            "tasks": sorted(self.tasks.keys()),
        }