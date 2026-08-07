"""
Sentinel DNA Runtime Agent Orchestrator

Enterprise agent execution coordinator.

Responsibilities:

- register runtime agents
- register lightweight capability agents
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

    @property
    def scheduler(self):
        """
        Backward compatibility layer.

        Older runtime components expect:

        orchestrator.scheduler.agents
        """

        return self.manager

    def register_agent(
        self,
        agent: Any,
        capabilities: list[str] | None = None,
    ) -> None:
        """
        Register runtime agent.

        Supports:

        - full runtime agents
        - lightweight gateway agents
        """

        if isinstance(agent, str):
            agent = SimpleRuntimeAgent(
                name=agent,
                capabilities=capabilities or [],
            )

        self.manager.register(agent)

    def execute(
        self,
        task: Any,
    ) -> Any:
        """
        Execute runtime task.
        """

        agents = self.manager.find_capability(
            task.capability
        )

        if not agents:
            return {
                "success": False,
                "error": (
                    f"No agent supports "
                    f"{task.capability}"
                ),
            }

        agent = agents[0]

        result = agent.execute(task)

        self.executions += 1

        return result

    def submit(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> str | None:
        """
        Submit capability request.

        Returns selected agent identity.

        Execution remains handled through execute().
        """

        agents = self.manager.find_capability(
            capability
        )

        if not agents:
            return None

        agent = agents[0]

        return self._agent_identity(agent)

    def _agent_identity(
        self,
        agent: Any,
    ) -> str | None:
        """
        Resolve agent identity safely.
        """

        return (
            getattr(agent, "name", None)
            or getattr(agent, "id", None)
            or str(agent)
        )

    def has_capability(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        return bool(
            self.manager.find_capability(
                capability
            )
        )

    def agent_count(
        self,
    ) -> int:
        """
        Return registered agent count.
        """

        return self.manager.count()

    def clear(
        self,
    ) -> None:
        """
        Clear runtime state.
        """

        self.manager.clear()

        self.executions = 0

    def count(
        self,
    ) -> int:
        """
        Return execution count.
        """

        return self.executions

    def status(
        self,
    ) -> dict[str, Any]:
        """
        Runtime status.
        """

        manager_status = self.manager.status()

        return {
            "agents": manager_status.get(
                "agents",
                0,
            ),
            "executions": self.executions,
            "manager": manager_status,
        }


@dataclass
class SimpleRuntimeAgent:
    """
    Lightweight capability agent.

    Used by gateway registration.
    """

    name: str

    capabilities: list[str]

    def execute(
        self,
        task: Any,
    ) -> dict[str, Any]:
        """
        Execute lightweight task.
        """

        return {
            "success": True,
            "agent": self.name,
            "capability": task.capability,
            "request": task.payload,
        }