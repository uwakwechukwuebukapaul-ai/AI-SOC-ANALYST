"""
Threat Intelligence Agent Tests
"""

from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.threat_intelligence_agent import (
    ThreatIntelligenceAgent,
)


def build_context():

    return AgentContext(
        investigation_id="INV-1001",
        case_id="CASE-1001",
        iocs=[
            "evil.com",
            "185.220.101.1",
            "google.com",
        ],
    )


def test_metadata():

    agent = ThreatIntelligenceAgent()

    assert agent.metadata.name == "Threat Intelligence Agent"

    assert agent.metadata.version == "1.0"

    assert "threat_intelligence" in agent.metadata.capabilities


def test_validate():

    agent = ThreatIntelligenceAgent()

    assert agent.validate(build_context())

    assert not agent.validate(None)


def test_execute():

    agent = ThreatIntelligenceAgent()

    result = agent.execute(build_context())

    assert result.successful()

    assert len(result.findings) == 3

    assert result.metadata["assessment_count"] == 3

    assert result.metadata["overall_threat"] == "critical"

    assert result.metadata["total_score"] == 225

    assert result.metadata["average_confidence"] > 0


def test_summary():

    agent = ThreatIntelligenceAgent()

    result = agent.execute(build_context())

    summary = agent.summarize(result)

    assert "Threat Intelligence completed" in summary

    assert "critical" in summary