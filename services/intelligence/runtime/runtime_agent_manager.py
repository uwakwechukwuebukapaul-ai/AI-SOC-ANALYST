"""
Runtime Agent Manager

Manages runtime intelligence agents,
registration, discovery, execution,
and lifecycle operations.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeAgentManager:
    """
    Runtime agent registry.
    """

    agents: dict[str, Any] = field(
        default_factory=dict
    )


    def register(
        self,
        agent: Any,
    ) -> None:
        """
        Register runtime agent.
        """

        name = self._agent_name(agent)

        self.agents[name] = agent


    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove runtime agent.
        """

        self.agents.pop(
            name,
            None,
        )


    def get(
        self,
        name: str,
    ) -> Any | None:
        """
        Retrieve agent.
        """

        return self.agents.get(
            name
        )


    def find_capability(
        self,
        capability: str,
    ) -> list[Any]:
        """
        Find agents supporting capability.
        """

        results = []

        for agent in self.agents.values():

            capabilities = self._capabilities(
                agent
            )

            if capability in capabilities:
                results.append(agent)

        return results


    def execute(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute capability using matching agent.
        """

        agents = self.find_capability(
            capability
        )

        if not agents:
            return {
                "success": False,
                "error": (
                    f"No agent supports {capability}"
                )
            }


        agent = agents[0]


        try:

            if hasattr(
                agent,
                "execute",
            ):

                return agent.execute(
                    payload
                )


            if callable(agent):

                return agent(
                    payload
                )


            return {
                "success": False,
                "error":
                    "Agent cannot execute",
            }


        except Exception as exc:

            return {
                "success": False,
                "error": str(exc),
            }


    def count(
        self,
    ) -> int:
        """
        Number of registered agents.
        """

        return len(
            self.agents
        )


    def clear(
        self,
    ) -> None:
        """
        Remove all agents.
        """

        self.agents.clear()


    def status(
        self,
    ) -> dict[str, Any]:
        """
        Runtime status.
        """

        return {
            "agents":
                len(self.agents),

            "count":
                len(self.agents),

            "names":
                list(
                    self.agents.keys()
                ),
        }


    def _agent_name(
        self,
        agent: Any,
    ) -> str:
        """
        Resolve agent name.
        """

        if hasattr(
            agent,
            "metadata",
        ):

            metadata = agent.metadata

            if hasattr(
                metadata,
                "name",
            ):
                return metadata.name


        if hasattr(
            agent,
            "name",
        ):
            return agent.name


        return agent.__class__.__name__


    def _capabilities(
        self,
        agent: Any,
    ) -> list[str]:
        """
        Resolve capabilities.
        """

        if hasattr(
            agent,
            "metadata",
        ):

            metadata = agent.metadata

            if hasattr(
                metadata,
                "capabilities",
            ):
                return metadata.capabilities


        if hasattr(
            agent,
            "capabilities",
        ):
            return agent.capabilities


        return []