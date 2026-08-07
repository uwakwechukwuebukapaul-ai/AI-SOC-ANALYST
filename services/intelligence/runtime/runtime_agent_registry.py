"""
Sentinel DNA Runtime Agent Registry

Enterprise runtime agent registry.

Responsibilities:

- register agents
- remove agents
- lookup agents
- track metadata
- expose registry status
"""


from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeAgentRegistry:
    """
    Runtime agent registry.
    """

    agents: dict[str, Any] = field(
        default_factory=dict
    )


    metadata: dict[str, dict] = field(
        default_factory=dict
    )


    def register(
        self,
        agent: Any,
    ) -> None:
        """
        Register runtime agent.
        """

        name = getattr(
            agent,
            "name",
            None,
        )

        if not name:
            raise ValueError(
                "Agent requires name"
            )


        self.agents[name] = agent


        self.metadata[name] = {
            "name": name,
            "capabilities": getattr(
                agent,
                "capabilities",
                [],
            ),
            "status": "active",
        }



    def get(
        self,
        name: str,
    ) -> Any | None:
        """
        Get agent.
        """

        return self.agents.get(
            name
        )



    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove agent.
        """

        self.agents.pop(
            name,
            None,
        )

        self.metadata.pop(
            name,
            None,
        )



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check agent existence.
        """

        return name in self.agents



    def clear(
        self,
    ) -> None:
        """
        Clear registry.
        """

        self.agents.clear()

        self.metadata.clear()



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Registry status.
        """

        return {
            "agents": len(
                self.agents
            ),
            "metadata": self.metadata,
        }