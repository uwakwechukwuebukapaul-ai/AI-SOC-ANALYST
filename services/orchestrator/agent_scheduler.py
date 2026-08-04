"""
Sentinel DNA
Enterprise Agent Scheduler

Coordinates execution of registered AI agents.

Author: Sentinel DNA
"""

from __future__ import annotations

from typing import Any, Dict

from .agent_registry import AgentRegistry
from .context import InvestigationContext


class AgentScheduler:
    """
    Controls agent execution routing.
    """


    def __init__(
        self,
        registry: AgentRegistry,
    ):
        self.registry = registry


    def schedule(
        self,
        agent_name: str,
        context: InvestigationContext,
    ) -> Dict[str, Any]:
        """
        Schedule an agent execution.
        """


        agent = self.registry.get_agent(
            agent_name
        )


        if not agent:
            raise ValueError(
                f"Agent '{agent_name}' not found"
            )


        if agent["status"] != "ACTIVE":
            raise RuntimeError(
                f"Agent '{agent_name}' unavailable"
            )


        return {
            "agent": agent_name,
            "status": "SCHEDULED",
            "investigation_id": (
                context.investigation_id
            ),
            "case_id": context.case_id,
        }