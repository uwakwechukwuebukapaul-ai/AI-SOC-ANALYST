"""
Sentinel DNA Runtime Agent Orchestrator

Enterprise runtime agent execution coordinator.

Responsibilities:

- Register runtime agents
- Route runtime tasks
- Track execution count
- Expose runtime status
- Coordinate runtime lifecycle
- Preserve compatibility with legacy scheduler access
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

    # ------------------------------------------------------------------
    # Compatibility
    # ------------------------------------------------------------------

    @property
    def scheduler(self) -> RuntimeAgentManager:
        """
        Backward-compatible scheduler interface.

        Older runtime components may expect:

            orchestrator.scheduler.agents
        """

        return self.manager

    # ------------------------------------------------------------------
    # Agent Lifecycle
    # ------------------------------------------------------------------

    def register_agent(
        self,
        agent: Any,
        capabilities: list[str] | None = None,
    ) -> Any:
        """
        Register a runtime agent.

        Supports normal runtime agents.

        A string may also be supplied as a lightweight compatibility
        registration and will be converted into SimpleRuntimeAgent.
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
        """
        Unregister a runtime agent.
        """

        return self.manager.unregister(name)

    def agent_count(self) -> int:
        """
        Return registered agent count.
        """

        return self.manager.count()

    def count_agents(self) -> int:
        """
        Backward-compatible alias for agent_count().
        """

        return self.agent_count()

    # ------------------------------------------------------------------
    # Capability
    # ------------------------------------------------------------------

    def has_capability(
        self,
        capability: str,
    ) -> bool:
        """
        Determine whether runtime can handle a capability.
        """

        return self.manager.has_capability(
            capability
        )

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def execute(
        self,
        task: Any,
    ) -> Any:
        """
        Execute a runtime task.

        Execution is delegated to RuntimeAgentManager.
        """

        result = self.manager.execute(
            task
        )

        self.executions += 1

        return result

    # ------------------------------------------------------------------
    # Submission
    # ------------------------------------------------------------------

    def submit(
        self,
        capability: str,
        request: dict[str, Any],
    ) -> str | None:
        """
        Select an agent capable of handling a request.

        Execution itself remains handled through execute().
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
        """
        Resolve agent identity safely.
        """

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

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Clear runtime state.
        """

        self.manager.clear()

        self.executions = 0

    # ------------------------------------------------------------------
    # Metrics
    # ------------------------------------------------------------------

    def count(self) -> int:
        """
        Return execution count.
        """

        return self.executions

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return runtime orchestrator status.
        """

        manager_status = self.manager.status()

        return {
            "agents": manager_status["agents"],
            "executions": self.executions,
            "manager": manager_status,
        }


@dataclass
class SimpleRuntimeAgent:
    """
    Lightweight runtime compatibility agent.

    Used when legacy code registers an agent by name and capability list.
    """

    name: str
    capabilities: list[str]

    def execute(
        self,
        task: Any,
    ) -> dict[str, Any]:
        """
        Execute a lightweight runtime task.
        """

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