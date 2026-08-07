"""
Controlled SOAR action execution boundary.

The initial implementation intentionally uses simulation mode.
Real EDR, IAM, firewall, email, and cloud integrations can be
introduced behind this interface without changing orchestration.
"""

from __future__ import annotations

from typing import Any, Callable


ActionHandler = Callable[[dict[str, Any]], dict[str, Any]]


class ActionExecutor:
    """Execute registered SOAR actions through controlled handlers."""

    def __init__(self, simulation: bool = True) -> None:
        self.simulation = simulation
        self._handlers: dict[str, ActionHandler] = {}

    def register_action(
        self,
        action: str,
        handler: ActionHandler,
    ) -> None:
        """Register an implementation for a SOAR action."""

        if not action or not action.strip():
            raise ValueError("Action name is required.")

        if not callable(handler):
            raise TypeError("Action handler must be callable.")

        self._handlers[action] = handler

    def available_actions(self) -> list[str]:
        """Return registered action names."""

        return sorted(self._handlers)

    def execute(
        self,
        action: str,
        target: str | None = None,
        parameters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute or simulate a SOAR action."""

        if action not in self._handlers:
            return {
                "action": action,
                "status": "unsupported",
                "target": target,
                "simulation": self.simulation,
            }

        payload = {
            "action": action,
            "target": target,
            "parameters": dict(parameters or {}),
        }

        if self.simulation:
            return {
                "action": action,
                "status": "simulated",
                "target": target,
                "parameters": dict(parameters or {}),
                "simulation": True,
            }

        result = self._handlers[action](payload)

        return {
            "action": action,
            "status": "executed",
            "target": target,
            "result": result,
            "simulation": False,
        }