"""
Sentinel DNA Runtime Engine

Central orchestration engine for
Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any
import time

from .task import Task
from .execution_result import ExecutionResult
from .execution_context import ExecutionContext
from .task_queue import TaskQueue
from .scheduler import Scheduler
from .event_bus import EventBus
from .runtime_metrics import RuntimeMetrics
from .memory import RuntimeMemory


@dataclass
class RuntimeEngine:
    """
    Intelligence execution runtime.
    """

    scheduler: Scheduler = field(
        default_factory=Scheduler
    )

    queue: TaskQueue = field(
        default_factory=TaskQueue
    )

    event_bus: EventBus = field(
        default_factory=EventBus
    )

    metrics: RuntimeMetrics = field(
        default_factory=RuntimeMetrics
    )

    memory: RuntimeMemory = field(
        default_factory=RuntimeMemory
    )

    context: ExecutionContext = field(
        default_factory=ExecutionContext
    )


    def submit(
        self,
        task: Task,
    ) -> None:
        """
        Submit task into runtime.
        """

        self.queue.enqueue(task)

        self.scheduler.schedule(task)

        self.event_bus.publish(
            "task_submitted",
            task,
        )


    def next_task(self) -> Task | None:
        """
        Retrieve next executable task.
        """

        return self.scheduler.next_task()


    def execute(
        self,
        task: Task,
        handler: Callable[
            [Task, ExecutionContext],
            Any
        ],
    ) -> ExecutionResult:
        """
        Execute task handler.
        """

        start_time = self.metrics.start_task()

        try:

            task.start()

            result = handler(
                task,
                self.context,
            )

            task.complete()

            duration = (
                time.perf_counter()
                - start_time
            )

            self.metrics.record_success(
                duration
            )

            self.event_bus.publish(
                "task_completed",
                task,
            )

            return ExecutionResult.ok(
                data={
                    "result": result
                }
            )


        except Exception as exc:

            duration = (
                time.perf_counter()
                - start_time
            )

            task.fail()

            self.metrics.record_failure(
                duration
            )

            self.event_bus.publish(
                "task_failed",
                task,
            )

            return ExecutionResult.failure(
                str(exc)
            )


    def set_memory(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.memory.set(
            key,
            value,
        )


    def get_memory(
        self,
        key: str,
        default=None,
    ):

        return self.memory.get(
            key,
            default,
        )


    def status(self) -> dict:

        return {
            "queue_size":
                self.queue.size(),

            "scheduled":
                self.scheduler.size(),

            "metrics":
                self.metrics.to_dict(),

            "memory":
                self.memory.to_dict(),
        }