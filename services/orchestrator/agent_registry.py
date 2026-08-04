"""
Sentinel DNA
Enterprise Agent Registry

Manages AI investigation agents,
their capabilities, and availability.

Author: Sentinel DNA
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List, Optional


def utc_now() -> str:
    """
    Returns timezone-aware UTC timestamp.
    """

    return datetime.now(timezone.utc).isoformat()


class AgentRegistry:
    """
    Central registry for investigation agents.

    Responsibilities:
    - Register agents
    - Discover agents
    - Search capabilities
    - Track availability
    """


    def __init__(self):
        self._agents: Dict[str, Dict] = {}


    def register_agent(
        self,
        name: str,
        capabilities: List[str],
    ) -> Dict:
        """
        Register a new investigation agent.
        """

        if name in self._agents:
            raise ValueError(
                f"Agent '{name}' already registered"
            )


        agent = {
            "name": name,
            "capabilities": capabilities,
            "status": "ACTIVE",
            "registered_at": utc_now(),
        }


        self._agents[name] = agent

        return agent



    def get_agent(
        self,
        name: str,
    ) -> Optional[Dict]:
        """
        Retrieve an agent by name.
        """

        return self._agents.get(name)



    def find_by_capability(
        self,
        capability: str,
    ) -> List[Dict]:
        """
        Find agents capable of performing
        a specific task.
        """

        return [
            agent
            for agent in self._agents.values()
            if capability in agent["capabilities"]
        ]



    def list_agents(self) -> List[Dict]:
        """
        Return all registered agents.
        """

        return list(
            self._agents.values()
        )



    def update_status(
        self,
        name: str,
        status: str,
    ) -> Dict:
        """
        Update agent availability state.
        """

        agent = self.get_agent(name)

        if not agent:
            raise KeyError(
                f"Agent '{name}' not found"
            )


        agent["status"] = status

        agent["updated_at"] = utc_now()

        return agent