"""
Sentinel DNA Agent Registry
"""

from __future__ import annotations

from dataclasses import dataclass, field

from services.intelligence.agents.base_agent import BaseAgent


@dataclass
class AgentRegistry:
    """
    Enterprise AI Agent Registry.
    """

    _agents: dict[str, BaseAgent] = field(
        default_factory=dict
    )

    def register(
        self,
        agent: BaseAgent,
    ) -> None:
        """
        Register an AI agent.
        """

        self._agents[
            agent.metadata.name
        ] = agent

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove an agent.
        """

        self._agents.pop(
            name,
            None,
        )

    def get(
        self,
        name: str,
    ) -> BaseAgent | None:
        """
        Retrieve an agent.
        """

        return self._agents.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether an agent exists.
        """

        return name in self._agents

    def list_agents(
        self,
    ) -> list[BaseAgent]:
        """
        Return registered agents.
        """

        return sorted(
            self._agents.values(),
            key=lambda agent: agent.metadata.name,
        )

    def find_by_capability(
        self,
        capability_name: str,
    ) -> list[BaseAgent]:
        """
        Find agents supporting a capability.
        """

        return [
            agent
            for agent in self._agents.values()
            if any(
                capability.name == capability_name
                for capability in agent.capabilities
            )
        ]

    def clear(
        self,
    ) -> None:
        """
        Remove all registered agents.
        """

        self._agents.clear()

    def count(
        self,
    ) -> int:
        """
        Number of registered agents.
        """

        return len(self._agents)