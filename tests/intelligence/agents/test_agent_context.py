"""
Tests for AgentContext.
"""

from services.intelligence.agents.agent_context import (
    AgentContext,
)


def test_defaults():

    context = AgentContext(
        investigation_id="INV-001",
        case_id="CASE-001",
    )

    assert context.alert == {}

    assert context.evidence == []


def test_shared_data():

    context = AgentContext(
        investigation_id="INV-001",
        case_id="CASE-001",
    )

    context.set(
        "risk_score",
        92,
    )

    assert context.get(
        "risk_score"
    ) == 92


def test_default_value():

    context = AgentContext(
        investigation_id="INV-001",
        case_id="CASE-001",
    )

    assert (
        context.get(
            "missing",
            "default",
        )
        == "default"
    )


def test_serialization():

    context = AgentContext(
        investigation_id="INV-001",
        case_id="CASE-001",
    )

    data = context.to_dict()

    assert data["case_id"] == "CASE-001"

    assert data["investigation_id"] == "INV-001"