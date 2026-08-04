"""
Sentinel DNA
Agent Scheduler Tests
"""

import pytest

from services.orchestrator.agent_registry import (
    AgentRegistry,
)

from services.orchestrator.agent_scheduler import (
    AgentScheduler,
)

from services.orchestrator.context import (
    InvestigationContext,
)


@pytest.fixture
def scheduler():

    registry = AgentRegistry()

    registry.register_agent(
        name="risk_engine",
        capabilities=[
            "risk_scoring"
        ],
    )

    return AgentScheduler(
        registry
    )


def test_schedule_active_agent(
    scheduler,
):

    context = InvestigationContext(
        investigation_id="INV-001"
    )


    result = scheduler.schedule(
        "risk_engine",
        context,
    )


    assert result["status"] == "SCHEDULED"

    assert (
        result["agent"]
        == "risk_engine"
    )


def test_schedule_unknown_agent(
    scheduler,
):

    context = InvestigationContext()


    with pytest.raises(ValueError):

        scheduler.schedule(
            "missing_agent",
            context,
        )