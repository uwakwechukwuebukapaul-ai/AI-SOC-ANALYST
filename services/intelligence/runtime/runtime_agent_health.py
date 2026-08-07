"""
Sentinel DNA Runtime Agent Health Manager

Tracks runtime agent health.

Responsibilities:

- track status
- record executions
- record failures
- expose health state
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentHealthRecord:
    """
    Agent health record.
    """

    agent_id: str

    status: str = "ACTIVE"

    executions: int = 0

    failures: int = 0


@dataclass
class RuntimeAgentHealthManager:
    """
    Runtime agent health manager.
    """

    agents: dict[str, AgentHealthRecord] = field(
        default_factory=dict
    )


    def register(
        self,
        agent_id: str,
    ) -> None:
        """
        Register health tracking.
        """

        if agent_id not in self.agents:
            self.agents[agent_id] = AgentHealthRecord(
                agent_id=agent_id
            )


    def record_execution(
        self,
        agent_id: str,
    ) -> None:
        """
        Record successful execution.
        """

        self.register(agent_id)

        self.agents[agent_id].executions += 1


    def record_failure(
        self,
        agent_id: str,
    ) -> None:
        """
        Record failed execution.
        """

        self.register(agent_id)

        self.agents[agent_id].failures += 1


    def set_status(
        self,
        agent_id: str,
        status: str,
    ) -> None:
        """
        Update agent status.
        """

        self.register(agent_id)

        self.agents[agent_id].status = status


    def get(
        self,
        agent_id: str,
    ) -> AgentHealthRecord | None:
        """
        Get health record.
        """

        return self.agents.get(
            agent_id
        )


    def clear(
        self,
    ) -> None:
        """
        Clear health state.
        """

        self.agents.clear()


    def status(
        self,
    ) -> dict[str, Any]:
        """
        Runtime health status.
        """

        return {
            "agents": len(
                self.agents
            ),
            "records": {
                key: vars(value)
                for key, value in self.agents.items()
            },
        }