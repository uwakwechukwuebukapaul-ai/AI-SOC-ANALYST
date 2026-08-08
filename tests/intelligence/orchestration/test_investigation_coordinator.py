"""
Sentinel DNA Investigation Coordinator Tests

Tests the investigation workflow boundary.
"""

from services.intelligence.orchestration import (
    InvestigationCoordinator,
)


class FakeAgent:
    def execute(self, context):
        return {
            "status": "success",
            "agent": "fake",
            "case_id": context.case_id,
        }


class FakeRegistry:
    def get(self, name):
        return FakeAgent()


def test_investigation():
    coordinator = InvestigationCoordinator(
        FakeRegistry()
    )

    result = coordinator.investigate(
        case_id="CASE-1001",
        alert={
            "title": "Suspicious PowerShell",
        },
    )

    assert result.success is True
    assert result.plan_name == (
        "Standard Security Investigation"
    )
    assert len(result.agents_executed) == 7


def test_investigation_results_are_aggregated():
    coordinator = InvestigationCoordinator(
        FakeRegistry()
    )

    result = coordinator.investigate(
        case_id="CASE-1002",
        alert={
            "title": "Suspicious PowerShell",
        },
    )

    assert result.success is True

    assert len(result.results) == 7

    assert (
        "IOC Agent"
        in result.results
    )

    assert (
        result.results["IOC Agent"]["status"]
        == "success"
    )


def test_investigation_result_contains_case_context():
    coordinator = InvestigationCoordinator(
        FakeRegistry()
    )

    result = coordinator.investigate(
        case_id="CASE-1003",
        alert={
            "title": "Malicious Script",
        },
    )

    assert result.success is True

    for agent_name in result.agents_executed:
        agent_result = result.results[
            agent_name
        ]

        assert (
            agent_result["case_id"]
            == "CASE-1003"
        )