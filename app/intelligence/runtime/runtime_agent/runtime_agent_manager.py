"""
Sentinel DNA Runtime Agent Manager

Enterprise runtime registry and capability router for AI agents.

Responsibilities:

- Register runtime agents
- Retrieve agents by name
- Unregister runtime agents
- Discover agents by capability
- Route runtime tasks
- Delegate execution to runtime agents
- Maintain runtime agent state

Architecture:
    RuntimeAgentManager
            |
            +-- Agent Registry
            |
            +-- Capability Discovery
            |
            +-- Task Routing
            |
            +-- Execution Delegation
"""

from __future__ import annotations

from typing import Any


class RuntimeAgentManager:
    """
    Manages AI agents registered inside the Sentinel DNA runtime.

    The manager owns registration, discovery, routing, and delegation.

    Individual agents remain responsible for their own execution
    infrastructure.
    """

    def __init__(self) -> None:
        self.agents: dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, agent: Any) -> Any:
        """
        Register a runtime agent.

        Supported identity sources:

        - agent.name
        - agent.metadata.name
        """

        name = self._agent_name(agent)

        if not name:
            raise ValueError("Agent must have a name")

        self.agents[name] = agent

        return agent

    def unregister(self, name: str) -> Any | None:
        """
        Remove and return an agent from the registry.
        """

        return self.agents.pop(name, None)

    def clear(self) -> None:
        """
        Remove all registered agents.
        """

        self.agents.clear()

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get(self, name: str) -> Any | None:
        """
        Retrieve an agent by name.
        """

        return self.agents.get(name)

    def list_agents(self) -> list[str]:
        """
        Return registered agent names.
        """

        return list(self.agents.keys())

    def count(self) -> int:
        """
        Return the number of registered agents.
        """

        return len(self.agents)

    # ------------------------------------------------------------------
    # Capability Discovery
    # ------------------------------------------------------------------

    def find_capability(
        self,
        capability: str,
    ) -> list[Any]:
        """
        Return all registered agents supporting a capability.
        """

        matches: list[Any] = []

        for agent in self.agents.values():

            capabilities = self._capabilities(agent)

            if capability in capabilities:
                matches.append(agent)

        return matches

    def has_capability(
        self,
        capability: str,
    ) -> bool:
        """
        Determine whether any registered agent supports a capability.
        """

        return bool(
            self.find_capability(capability)
        )

    # ------------------------------------------------------------------
    # Task Execution
    # ------------------------------------------------------------------

    def execute(
        self,
        task: Any,
    ) -> Any:
        """
        Route and execute a runtime task.

        The task must expose:

            task.capability

        and may expose:

            task.payload
        """

        capability = getattr(
            task,
            "capability",
            None,
        )

        if not capability:
            raise ValueError(
                "Task must define a capability"
            )

        agents = self.find_capability(
            capability
        )

        if not agents:
            raise LookupError(
                "No runtime agent available for "
                f"capability '{capability}'"
            )

        agent = agents[0]

        return self._execute_agent(
            agent,
            task,
            capability,
        )

    # ------------------------------------------------------------------
    # Agent Execution Resolution
    # ------------------------------------------------------------------

    def _execute_agent(
        self,
        agent: Any,
        task: Any,
        capability: str,
    ) -> Any:
        """
        Resolve the execution interface exposed by an agent.

        Preferred interface:

            agent.execute(task)

        Gateway fallback:

            agent.gateway.execution.workers.executor.execute(
                capability,
                payload,
            )
        """

        execute = getattr(
            agent,
            "execute",
            None,
        )

        if callable(execute):
            return execute(task)

        gateway = getattr(
            agent,
            "gateway",
            None,
        )

        if gateway is None:
            raise AttributeError(
                f"Runtime agent '{self._agent_name(agent)}' "
                "does not expose an execution interface"
            )

        execution = getattr(
            gateway,
            "execution",
            None,
        )

        if execution is None:
            raise AttributeError(
                f"Runtime agent '{self._agent_name(agent)}' "
                "does not expose gateway execution"
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
            payload = getattr(
                task,
                "payload",
                task,
            )

            return execute_method(
                capability,
                payload,
            )

        raise AttributeError(
            f"Runtime agent '{self._agent_name(agent)}' "
            "does not expose a supported execution method"
        )

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return runtime manager status.
        """

        return {
            "agents": self.list_agents(),
            "count": self.count(),
        }

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _agent_name(
        agent: Any,
    ) -> str:
        """
        Resolve an agent identity.
        """

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
        Resolve agent capabilities.

        Supported sources:

        - agent.capabilities
        - agent.metadata.capabilities
        """

        capabilities = getattr(
            agent,
            "capabilities",
            None,
        )

        if capabilities is not None:
            return list(capabilities)

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

        if capabilities is not None:
            return list(capabilities)

        return []