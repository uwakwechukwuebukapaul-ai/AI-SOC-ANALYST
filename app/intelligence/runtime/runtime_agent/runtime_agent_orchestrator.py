"""
Sentinel DNA Runtime Agent Orchestrator

Canonical runtime agent execution coordinator.
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

    @property
    def scheduler(self) -> RuntimeAgentManager:
        """
        Backward-compatible scheduler interface.
        """

        return self.manager

    def register_agent(
        self,
        agent: Any,
        capabilities: list[str] | None = None,
    ) -> Any:
        """
        Register runtime agent.

        String registrations are converted into
        SimpleRuntimeAgent instances.
        """

        if isinstance(agent, str):
            agent = SimpleRuntimeAgent(
                name=agent,
                capabilities=capabilities or [],
            )

        return self.manager.register(agent)

    def unregister_agent(
        self,
        name: str,
    ) -> Any | None:
        """Unregister an agent."""

        return self.manager.unregister(name)

    def agent_count(self) -> int:
        """Return registered agent count."""

        return self.manager.count()

    def count_agents(self) -> int:
        """Backward-compatible agent count alias."""

        return self.agent_count()

    def has_capability(
        self,
        capability: str,
    ) -> bool:
        """Determine capability availability."""

        return self.manager.has_capability(
            capability
        )

    def execute(
        self,
        task: Any,
    ) -> Any:
        """Execute a runtime task."""

        result = self.manager.execute(task)

        self.executions += 1

        return result

    def submit(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> str | None:
        """
        Select an agent capable of handling a request.

        This method intentionally performs selection only.
        """

        agents = self.manager.find_capability(
            capability
        )

        if not agents:
            return None

        return self._agent_identity(
            agents[0]
        )

    @staticmethod
    def _agent_identity(
        agent: Any,
    ) -> str | None:
        """Resolve agent identity."""

        name = getattr(
            agent,
            "name",
            None,
        )

        if name:
            return str(name)

        agent_id = getattr(
            agent,
            "id",
            None,
        )

        if agent_id:
            return str(agent_id)

        return str(agent)

    def clear(self) -> None:
        """Clear runtime state."""

        self.manager.clear()
        self.executions = 0

    def count(self) -> int:
        """Return execution count."""

        return self.executions

    def status(self) -> dict[str, Any]:
        """Return runtime status."""

        manager_status = self.manager.status()

        return {
            "agents": manager_status["agents"],
            "executions": self.executions,
            "manager": manager_status,
        }


@dataclass
class SimpleRuntimeAgent:
    """
    Lightweight compatibility runtime agent.
    """

    name: str
    capabilities: list[str]

    def execute(
        self,
        task: Any,
    ) -> dict[str, Any]:
        """Execute a lightweight runtime task."""

        return {
            "success": True,
            "agent": self.name,
            "capability": task.capability,
            "request": getattr(
                task,
                "payload",
                {},
            ),
        }