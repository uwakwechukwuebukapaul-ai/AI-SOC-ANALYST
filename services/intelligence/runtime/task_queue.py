"""
Sentinel DNA Runtime Task Queue
"""

from __future__ import annotations

from collections import deque

from services.intelligence.runtime.task import Task


class TaskQueue:
    """
    FIFO queue for runtime tasks.
    """

    def __init__(self) -> None:
        self._queue: deque[Task] = deque()

    def enqueue(self, task: Task) -> None:
        self._queue.append(task)

    def dequeue(self) -> Task | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def peek(self) -> Task | None:
        if not self._queue:
            return None
        return self._queue[0]

    def size(self) -> int:
        return len(self._queue)

    def empty(self) -> bool:
        return len(self._queue) == 0

    def clear(self) -> None:
        self._queue.clear()

    def tasks(self) -> list[Task]:
        return list(self._queue)