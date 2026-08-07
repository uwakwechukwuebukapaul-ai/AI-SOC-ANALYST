"""
Sentinel DNA SOAR automation orchestration engine.
"""

from __future__ import annotations

from typing import Any

from .action_executor import ActionExecutor
from .playbook_engine import PlaybookEngine
from .response_history import ResponseHistory


class AutomationEngine:
    """
    Orchestrates security-response playbooks.

    The engine deliberately separates:
        1. playbook selection,
        2. action execution,
        3. response auditing.
    """

    def __init__(
        self,
        *,
        playbook_engine: PlaybookEngine | None = None,
        action_executor: ActionExecutor | None = None,
        response_history: ResponseHistory | None = None,
    ) -> None:
        self.playbooks = playbook_engine or PlaybookEngine()
        self.executor = action_executor or ActionExecutor()
        self.history = response_history or ResponseHistory()

    def register_playbook(
        self,
        name: str,
        trigger: str,
        actions: list[str],
        description: str = "",
    ) -> dict[str, Any]:
        """Register a response playbook."""

        return self.playbooks.register(
            name=name,
            trigger=trigger,
            actions=actions,
            description=description,
        )

    def execute_playbook(
        self,
        playbook_name: str,
        *,
        case_id: str | None = None,
        target: str | None = None,
        parameters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a registered playbook."""

        playbook = self.playbooks.get(playbook_name)

        if playbook is None:
            raise ValueError(
                f"Unknown SOAR playbook: {playbook_name}"
            )

        results: list[dict[str, Any]] = []

        for action in playbook["actions"]:
            result = self.executor.execute(
                action=action,
                target=target,
                parameters=parameters,
            )

            history_record = self.history.record(
                action=action,
                status=result["status"],
                case_id=case_id,
                target=target,
                details=result,
            )

            results.append(history_record)

        return {
            "playbook": playbook_name,
            "case_id": case_id,
            "target": target,
            "status": "completed",
            "actions": results,
        }

    def response_history(
        self,
        case_id: str | None = None,
    ) -> list[dict[str, Any]]:
        """Return response history."""

        if case_id is None:
            return self.history.all()

        return self.history.for_case(case_id)