"""
Tests for InvestigationAgent.
"""

from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
)
from services.intelligence.agents.investigation_agent import (
    InvestigationAgent,
)


def build_context():

    return AgentContext(
        investigation_id="INV-1001",
        case_id="CASE-1001",
    )


def test_metadata():

    agent = InvestigationAgent()

    assert agent.metadata.name == "Investigation Agent"


def test_validate():

    agent = InvestigationAgent()

    assert agent.validate(build_context())


def test_execute():

    agent = InvestigationAgent()

    result = agent.execute(build_context())

    assert result.status == AgentExecutionStatus.SUCCESS

    assert "investigation_plan" in result.artifacts


def test_summary():

    agent = InvestigationAgent()

    result = agent.execute(build_context())

    assert "steps" in agent.summarize(result)