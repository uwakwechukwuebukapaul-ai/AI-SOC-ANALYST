"""
Tests for AgentResult.
"""

from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)


def test_defaults():

    result = AgentResult(
        agent_name="IOC Agent",
        status=AgentExecutionStatus.SUCCESS,
    )

    assert result.confidence == 0.0

    assert result.successful() is True


def test_findings():

    result = AgentResult(
        agent_name="MITRE",
        status=AgentExecutionStatus.SUCCESS,
    )

    result.add_finding(
        {
            "technique": "T1059"
        }
    )

    assert len(result.findings) == 1


def test_recommendations():

    result = AgentResult(
        agent_name="Threat Intel",
        status=AgentExecutionStatus.SUCCESS,
    )

    result.add_recommendation(
        "Isolate endpoint"
    )

    assert (
        result.recommendations[0]
        == "Isolate endpoint"
    )


def test_errors():

    result = AgentResult(
        agent_name="Timeline",
        status=AgentExecutionStatus.FAILED,
    )

    result.add_error(
        "Missing evidence"
    )

    assert len(result.errors) == 1


def test_serialization():

    result = AgentResult(
        agent_name="Report",
        status=AgentExecutionStatus.SUCCESS,
        confidence=97.5,
    )

    data = result.to_dict()

    assert data["confidence"] == 97.5

    assert data["status"] == "success"