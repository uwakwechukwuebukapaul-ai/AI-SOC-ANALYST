"""
Sentinel DNA Runtime Agent Orchestrator

Enterprise agent execution coordinator.

Responsibilities:

- register runtime agents
- execute agent tasks
- route capability execution
- maintain execution count
- expose runtime status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_manager import RuntimeAgentManager


@dataclass
class RuntimeAgentOrchestrator:
    """
    Coordinates runtime agent execution.
    """

    manager: RuntimeAgentManager = field(
        default_factory=RuntimeAgentManager
    )

    executions: int = 0

    def register_agent(
        self,
        agent: Any,
    ) -> None:
        """
        Register runtime agent.
        """

        self.manager.register(agent)

    def execute(
        self,
        task: Any,
    ) -> Any:
        """
        Execute task through agent manager.
        """

        result = self.manager.execute(task)

        self.executions += 1

        return result

    def clear(self) -> None:
        """
        Clear runtime state.
        """

        self.manager.clear()

        self.executions = 0

    def count(self) -> int:
        """
        Return execution count.
        """

        return self.executions

    def status(self) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {
            "executions": self.executions,
            "manager": self.manager.status(),
        }