"""
Sentinel DNA Investigation Planner
"""

from __future__ import annotations

from services.intelligence.agents.agent_registry import AgentRegistry
from services.intelligence.planning.investigation_plan import (
    InvestigationPlan,
    InvestigationStep,
)


class InvestigationPlanner:
    """
    Builds execution plans from registered agents.
    """

    def __init__(self, registry: AgentRegistry):
        self._registry = registry

    def build_plan(self) -> InvestigationPlan:
        plan = InvestigationPlan()

        for agent in self._registry.list_agents():
            for capability in agent.capabilities:
                plan.add_step(
                    InvestigationStep(
                        agent_name=agent.metadata.name,
                        capability=capability.name,
                        parallel=capability.parallel_execution,
                    )
                )

        return plan