"""
Tests for AgentMetadata.
"""

from services.intelligence.agents.agent_metadata import (
    AgentMetadata,
)


def test_defaults():

    metadata = AgentMetadata(
        name="IOC Agent",
        version="1.0",
        description="IOC enrichment",
    )

    assert metadata.author == "Sentinel DNA"

    assert metadata.experimental is False


def test_capabilities():

    metadata = AgentMetadata(
        name="MITRE",
        version="1.0",
        description="Mapping",
        capabilities=[
            "mitre_mapping",
            "attack_analysis",
        ],
    )

    assert len(metadata.capabilities) == 2


def test_tags():

    metadata = AgentMetadata(
        name="Threat Intel",
        version="1.0",
        description="Intel",
        tags=[
            "enterprise",
            "threat",
        ],
    )

    assert "enterprise" in metadata.tags


def test_to_dict():

    metadata = AgentMetadata(
        name="Investigation",
        version="2.0",
        description="Coordinator",
    )

    data = metadata.to_dict()

    assert data["name"] == "Investigation"

    assert data["version"] == "2.0"

    assert "description" in data