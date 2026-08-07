"""
Tests for AgentCapability.
"""

from services.intelligence.agents.agent_capability import (
    AgentCapability,
)


def test_defaults():

    capability = AgentCapability(
        name="IOC Enrichment",
        description="Enrich indicators",
        category="intelligence",
    )

    assert capability.priority == 100

    assert capability.enabled is True


def test_inputs_outputs():

    capability = AgentCapability(
        name="MITRE",
        description="Map ATT&CK",
        category="analysis",
        required_inputs=["ioc"],
        produced_outputs=["techniques"],
    )

    assert capability.required_inputs == ["ioc"]

    assert capability.produced_outputs == [
        "techniques"
    ]


def test_serialization():

    capability = AgentCapability(
        name="Reporting",
        description="Generate report",
        category="reporting",
    )

    data = capability.to_dict()

    assert data["name"] == "Reporting"

    assert data["category"] == "reporting"

    assert "priority" in data