from services.intelligence.agents.agent_registry import AgentRegistry
from services.intelligence.agents.investigation_agent import (
    InvestigationAgent,
)
from services.intelligence.planning.investigation_planner import (
    InvestigationPlanner,
)


def test_build_plan():

    registry = AgentRegistry()

    registry.register(InvestigationAgent())

    planner = InvestigationPlanner(registry)

    plan = planner.build_plan()

    assert len(plan) > 0