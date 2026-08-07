"""
Sentinel DNA Workflow Executor

Executes intelligence workflows using
the runtime execution framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any

from .runtime_api import RuntimeAPI
from .task import Task


@dataclass
class WorkflowExecutor:
    """
    Executes multi-step intelligence workflows.
    """

    runtime: RuntimeAPI = field(
        default_factory=RuntimeAPI
    )

    workflows: dict[str, list[Task]] = field(
        default_factory=dict
    )


    def register_workflow(
        self,
        workflow_id: str,
        tasks: list[Task],
    ) -> None:
        """
        Register workflow tasks.
        """

        self.workflows[workflow_id] = tasks



    def execute_workflow(
        self,
        workflow_id: str,
        handler: Callable[
            [Task, Any],
            Any
        ],
    ) -> list:

        results = []

        tasks = self.workflows.get(
            workflow_id,
            []
        )

        for task in tasks:

            self.runtime.submit_task(task)

            result = self.runtime.execute(
                task,
                handler,
            )

            results.append(result)


        return results



    def status(self) -> dict:

        return {
            "workflow_count":
                len(self.workflows),

            "workflows":
                list(self.workflows.keys()),
        }