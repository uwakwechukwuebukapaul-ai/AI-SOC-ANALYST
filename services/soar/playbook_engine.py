"""
SOAR playbook definition and validation engine.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


class PlaybookEngine:
    """Manage and validate security-response playbooks."""

    REQUIRED_FIELDS = {"name", "trigger", "actions"}

    def __init__(self) -> None:
        self._playbooks: dict[str, dict[str, Any]] = {}

    def register(
        self,
        name: str,
        trigger: str,
        actions: list[str],
        description: str = "",
    ) -> dict[str, Any]:
        """Register a new playbook."""

        if not name or not name.strip():
            raise ValueError("Playbook name is required.")

        if not trigger or not trigger.strip():
            raise ValueError("Playbook trigger is required.")

        if not actions:
            raise ValueError("Playbook must contain at least one action.")

        playbook = {
            "name": name,
            "trigger": trigger,
            "actions": list(actions),
            "description": description,
        }

        self._playbooks[name] = playbook

        return deepcopy(playbook)

    def get(self, name: str) -> dict[str, Any] | None:
        """Return a registered playbook."""

        playbook = self._playbooks.get(name)

        return deepcopy(playbook) if playbook else None

    def list_playbooks(self) -> list[dict[str, Any]]:
        """Return all registered playbooks."""

        return deepcopy(list(self._playbooks.values()))

    def validate(self, playbook: dict[str, Any]) -> bool:
        """Validate playbook structure."""

        if not isinstance(playbook, dict):
            return False

        if not self.REQUIRED_FIELDS.issubset(playbook):
            return False

        if not isinstance(playbook["actions"], list):
            return False

        if not playbook["name"]:
            return False

        if not playbook["trigger"]:
            return False

        return bool(playbook["actions"])