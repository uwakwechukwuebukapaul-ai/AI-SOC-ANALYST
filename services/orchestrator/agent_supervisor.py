"""
Sentinel DNA
Enterprise Agent Supervisor

Responsible for:
- Monitoring agent execution
- Tracking agent health
- Managing agent lifecycle
- Coordinating recovery actions

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class AgentHealth:
    """
    Agent operational health state.
    """

    agent_name: str

    status: str = "ACTIVE"

    executions: int = 0

    failures: int = 0

    last_error: Optional[str] = None

    last_seen: str = field(default_factory=utc_now)


class AgentSupervisor:
    """
    Enterprise agent supervision layer.

    Provides:
    - health monitoring
    - failure tracking
    - availability checks
    - lifecycle control
    """

    def __init__(self):

        self.agents: Dict[str, AgentHealth] = {}


    def register_agent(
        self,
        agent_name: str
    ) -> AgentHealth:

        if agent_name in self.agents:
            return self.agents[agent_name]

        health = AgentHealth(
            agent_name=agent_name
        )

        self.agents[agent_name] = health

        return health


    def record_execution(
        self,
        agent_name: str
    ) -> AgentHealth:

        agent = self._get_agent(agent_name)

        agent.executions += 1

        agent.status = "ACTIVE"

        agent.last_seen = utc_now()

        return agent


    def record_failure(
        self,
        agent_name: str,
        error: str
    ) -> AgentHealth:

        agent = self._get_agent(agent_name)

        agent.failures += 1

        agent.last_error = error

        agent.status = "DEGRADED"

        agent.last_seen = utc_now()

        return agent


    def get_health(
        self,
        agent_name: str
    ) -> Dict[str, Any]:

        agent = self._get_agent(agent_name)

        return {

            "agent_name": agent.agent_name,

            "status": agent.status,

            "executions": agent.executions,

            "failures": agent.failures,

            "last_error": agent.last_error,

            "last_seen": agent.last_seen,

        }


    def list_agents(self) -> List[Dict[str, Any]]:

        return [
            self.get_health(name)
            for name in self.agents
        ]


    def is_available(
        self,
        agent_name: str
    ) -> bool:

        agent = self._get_agent(agent_name)

        return agent.status == "ACTIVE"


    def reset_agent(
        self,
        agent_name: str
    ) -> AgentHealth:

        agent = self._get_agent(agent_name)

        agent.status = "ACTIVE"

        agent.last_error = None

        agent.last_seen = utc_now()

        return agent


    def _get_agent(
        self,
        agent_name: str
    ) -> AgentHealth:

        if agent_name not in self.agents:

            raise ValueError(
                f"Unknown agent: {agent_name}"
            )

        return self.agents[agent_name]