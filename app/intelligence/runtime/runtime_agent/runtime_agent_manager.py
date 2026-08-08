"""
Sentinel DNA Runtime Agent Manager

Canonical registry and execution manager for runtime agents.
"""

from __future__ import annotations

from typing import Any

from ..task import Task


class RuntimeAgentManager:
    """
    Manage registered runtime agents and execute tasks against them.
    """

    def __init__(self) -> None:
        self.agents: dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, agent: Any) -> Any:
        """
        Register an agent.

        Agent identity is resolved from:

        1. agent.name
        2. agent.metadata.name
        3. class name
        """

        name = self._agent_name(agent)

        if name in self.agents:
            raise ValueError(
                f"Runtime agent '{name}' is already registered."
            )

        self.agents[name] = agent

        return agent

    def unregister(self, name: str) -> Any | None:
        """
        Remove an agent by name.
        """

        return self.agents.pop(name, None)

    def clear(self) -> None:
        """Remove all registered agents."""

        self.agents.clear()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def count(self) -> int:
        """Return registered agent count."""

        return len(self.agents)

    def list_agents(self) -> list[str]:
        """Return registered agent names."""

        return list(self.agents.keys())

    def find_capability(
        self,
        capability: str,
    ) -> list[Any]:
        """
        Return agents supporting a capability.
        """

        if not capability:
            return []

        return [
            agent
            for agent in self.agents.values()
            if capability in self._capabilities(agent)
        ]

    def has_capability(
        self,
        capability: str,
    ) -> bool:
        """Return whether a capability is available."""

        return bool(
            self.find_capability(capability)
        )

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def execute(
        self,
        task: Task,
    ) -> Any:
        """
        Execute a task using the first capable runtime agent.
        """

        if not isinstance(task, Task):
            raise TypeError(
                "RuntimeAgentManager.execute() requires a Task."
            )

        agents = self.find_capability(
            task.capability
        )

        if not agents:
            raise LookupError(
                "No runtime agent supports capability "
                f"'{task.capability}'."
            )

        agent = agents[0]

        task.queue()
        task.start()

        try:
            result = self._execute_agent(
                agent,
                task,
            )

            task.complete()

            return result

        except Exception:
            task.fail()
            raise

    def _execute_agent(
        self,
        agent: Any,
        task: Task,
    ) -> Any:
        """
        Resolve a supported agent execution interface.
        """

        execute = getattr(
            agent,
            "execute",
            None,
        )

        if callable(execute):
            return execute(task)

        execution = getattr(
            agent,
            "execution",
            None,
        )

        if execution is None:
            raise AttributeError(
                f"Runtime agent '{self._agent_name(agent)}' "
                "does not expose execution workers"
            )

        workers = getattr(
            execution,
            "workers",
            None,
        )

        if workers is None:
            raise AttributeError(
                f"Runtime agent '{self._agent_name(agent)}' "
                "does not expose execution workers"
            )

        executor = getattr(
            workers,
            "executor",
            None,
        )

        if executor is None:
            raise AttributeError(
                f"Runtime agent '{self._agent_name(agent)}' "
                "does not expose an executor"
            )

        execute_method = getattr(
            executor,
            "execute",
            None,
        )

        if callable(execute_method):
            return execute_method(
                task.capability,
                task.payload,
            )

        raise AttributeError(
            f"Runtime agent '{self._agent_name(agent)}' "
            "does not expose a supported execution method"
        )

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """Return manager status."""

        return {
            "agents": self.list_agents(),
            "count": self.count(),
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _agent_name(
        agent: Any,
    ) -> str:
        """Resolve agent identity."""

        name = getattr(
            agent,
            "name",
            None,
        )

        if name:
            return str(name)

        metadata = getattr(
            agent,
            "metadata",
            None,
        )

        metadata_name = getattr(
            metadata,
            "name",
            None,
        )

        if metadata_name:
            return str(metadata_name)

        return agent.__class__.__name__

    @staticmethod
    def _capabilities(
        agent: Any,
    ) -> list[str]:
        """
        Resolve capabilities.

        Supports:

        agent.capabilities
        agent.metadata.capabilities

        Capability objects with a `.name` attribute are also supported.
        """

        capabilities = getattr(
            agent,
            "capabilities",
            None,
        )

        if capabilities is None:
            metadata = getattr(
                agent,
                "metadata",
                None,
            )

            capabilities = getattr(
                metadata,
                "capabilities",
                None,
            )

        if capabilities is None:
            return []

        resolved: list[str] = []

        for capability in capabilities:
            if isinstance(capability, str):
                resolved.append(capability)
                continue

            name = getattr(
                capability,
                "name",
                None,
            )

            if name:
                resolved.append(str(name))

        return resolved