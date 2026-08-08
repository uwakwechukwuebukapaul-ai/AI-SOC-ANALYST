"""
Sentinel DNA Workflow Executor

Executes multi-step intelligence workflows using
the runtime execution framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_api import RuntimeAPI
from .task import Task


@dataclass
class WorkflowExecutor:
    """
    Executes registered multi-step intelligence workflows.

    A workflow is represented as an ordered collection of
    canonical runtime Task objects.

    Responsibilities:

    - register workflows
    - preserve workflow task ordering
    - execute registered tasks
    - expose workflow runtime status
    """

    runtime: RuntimeAPI = field(
        default_factory=RuntimeAPI
    )

    workflows: dict[str, list[Task]] = field(
        default_factory=dict
    )

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register_workflow(
        self,
        workflow_id: str,
        tasks: list[Task],
    ) -> None:
        """
        Register a workflow and its runtime tasks.

        Tasks are copied into a new list so callers cannot
        accidentally mutate the registered workflow ordering.
        """

        if not workflow_id or not workflow_id.strip():
            raise ValueError(
                "Workflow ID is required."
            )

        if tasks is None:
            raise ValueError(
                "Workflow tasks are required."
            )

        if not isinstance(tasks, list):
            raise TypeError(
                "Workflow tasks must be provided as a list."
            )

        for task in tasks:
            if not isinstance(task, Task):
                raise TypeError(
                    "Workflow tasks must contain Task instances."
                )

        self.workflows[workflow_id] = list(tasks)

    def unregister_workflow(
        self,
        workflow_id: str,
    ) -> list[Task] | None:
        """
        Remove a registered workflow.

        Returns the removed task list or None when the
        workflow does not exist.
        """

        return self.workflows.pop(
            workflow_id,
            None,
        )

    def has_workflow(
        self,
        workflow_id: str,
    ) -> bool:
        """
        Return whether a workflow is registered.
        """

        return workflow_id in self.workflows

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def execute_workflow(
        self,
        workflow_id: str,
        handler: Callable[
            [Task, Any],
            Any,
        ],
    ) -> list[Any]:
        """
        Execute all tasks registered under a workflow.

        Tasks are executed in registration order.
        """

        if not workflow_id or not workflow_id.strip():
            raise ValueError(
                "Workflow ID is required."
            )

        if not callable(handler):
            raise TypeError(
                "Workflow handler must be callable."
            )

        tasks = self.workflows.get(
            workflow_id,
            [],
        )

        results: list[Any] = []

        for task in tasks:
            self.runtime.submit_task(
                task
            )

            result = self.runtime.execute(
                task,
                handler,
            )

            results.append(
                result
            )

        return results

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Clear all registered workflows.
        """

        self.workflows.clear()

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return workflow executor status.
        """

        return {
            "workflow_count": len(
                self.workflows
            ),
            "workflows": list(
                self.workflows.keys()
            ),
        }