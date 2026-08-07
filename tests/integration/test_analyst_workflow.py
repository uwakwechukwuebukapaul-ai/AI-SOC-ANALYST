"""
Analyst Workflow Integration Tests

Validates SOC analyst investigation lifecycle.
"""


from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)

from services.investigation.autonomous_investigation_intelligence_engine import (
    AutonomousInvestigationIntelligenceEngine,
)

from services.response.autonomous_security_response_engine import (
    AutonomousSecurityResponseEngine,
)


def test_create_security_case():

    coordinator = AutonomousAgentCoordinator()

    case = coordinator.coordinate_workflow(
        [
            "receive_alert",
            "collect_evidence",
            "analyze_threat",
        ]
    )

    assert case["status"] == "completed"
    assert len(case["steps"]) == 3


def test_assign_investigation_agent():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "investigator-001",
        "investigation"
    )

    task = coordinator.assign_task(
        "investigator-001",
        "Analyze suspicious login activity"
    )

    assert task["status"] == "assigned"


def test_ai_investigation_component():

    engine = AutonomousInvestigationIntelligenceEngine()

    assert engine is not None


def test_response_recommendation_component():

    engine = AutonomousSecurityResponseEngine()

    assert engine is not None


def test_complete_analyst_flow():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "soc-agent",
        "security_operations"
    )

    workflow = coordinator.coordinate_workflow(
        [
            "alert_triage",
            "investigation",
            "response",
            "report"
        ]
    )

    assert workflow["status"] == "completed"

    status = coordinator.system_status()

    assert status["agents"] == 1
    assert status["workflows"] == 1