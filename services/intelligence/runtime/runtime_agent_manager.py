"""
Sentinel DNA Runtime Agent Manager

Enterprise AI agent management layer.

Responsibilities:

- register agents
- discover capabilities
- route tasks
- manage agent lifecycle
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_runtime import (
    RuntimeAgentRuntime,
)

from .task import (
    Task,
)



@dataclass
class RuntimeAgentManager:
    """
    Multi-agent runtime manager.
    """

    agents: dict[str, RuntimeAgentRuntime] = field(
        default_factory=dict
    )


    def register(
        self,
        agent: RuntimeAgentRuntime,
    ) -> None:
        """
        Register AI agent.
        """

        self.agents[agent.name] = agent



    def get(
        self,
        name: str,
    ) -> RuntimeAgentRuntime | None:
        """
        Retrieve agent.
        """

        return self.agents.get(
            name
        )



    def find_capability(
        self,
        capability: str,
    ) -> list[RuntimeAgentRuntime]:
        """
        Find agents supporting capability.
        """

        return [
            agent
            for agent in self.agents.values()
            if agent.can_execute(
                capability
            )
        ]



    def execute(
        self,
        task: Task,
    ) -> Any:
        """
        Route task to capable agent.
        """

        agents = self.find_capability(
            task.capability
        )


        if not agents:
            return None


        return agents[0].execute(
            task
        )



    def unregister(
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



    def clear(self) -> None:
        """
        Remove all agents.
        """

        self.agents.clear()



    def count(self) -> int:
        """
        Return agent count.
        """

        return len(
            self.agents
        )



    def status(self) -> dict[str, Any]:
        """
        Agent manager status.
        """

        return {
            "agents":
                list(
                    self.agents.keys()
                ),

            "count":
                self.count(),
        }