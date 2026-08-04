"""
Sentinel DNA
Agent Registry Tests

Validates agent registration,
lookup, capability discovery,
and duplicate protection.

Author: Sentinel DNA
"""

import pytest

from services.orchestrator.agent_registry import (
    AgentRegistry,
)


@pytest.fixture
def registry():
    """
    Creates a fresh agent registry.
    """

    return AgentRegistry()


def test_register_agent(registry):
    """
    Agent should register successfully.
    """

    agent = registry.register_agent(
        name="threat_classifier",
        capabilities=[
            "classification",
            "threat_analysis",
        ],
    )

    assert agent["name"] == "threat_classifier"

    assert (
        "classification"
        in agent["capabilities"]
    )


def test_lookup_agent(registry):
    """
    Registered agent should be discoverable.
    """

    registry.register_agent(
        name="ioc_enrichment",
        capabilities=[
            "ioc_lookup",
        ],
    )

    agent = registry.get_agent(
        "ioc_enrichment"
    )

    assert agent is not None

    assert (
        agent["name"]
        == "ioc_enrichment"
    )


def test_duplicate_agent_registration_blocked(registry):
    """
    Duplicate agent names should not be allowed.
    """

    registry.register_agent(
        name="risk_engine",
        capabilities=[
            "risk_scoring",
        ],
    )

    with pytest.raises(Exception):
        registry.register_agent(
            name="risk_engine",
            capabilities=[
                "duplicate",
            ],
        )


def test_agent_capability_search(registry):
    """
    Registry should find agents by capability.
    """

    registry.register_agent(
        name="mitre_mapper",
        capabilities=[
            "attack_mapping",
            "technique_detection",
        ],
    )

    agents = registry.find_by_capability(
        "attack_mapping"
    )

    assert len(agents) == 1

    assert (
        agents[0]["name"]
        == "mitre_mapper"
    )


def test_agent_status(registry):
    """
    Registered agents should expose availability state.
    """

    agent = registry.register_agent(
        name="response_agent",
        capabilities=[
            "containment",
        ],
    )

    assert (
        agent["status"]
        == "ACTIVE"
    )