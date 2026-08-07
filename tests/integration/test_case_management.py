"""
Case Management Integration Tests

Validates security case lifecycle.
"""


from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)


def test_case_creation():

    coordinator = AutonomousAgentCoordinator()

    case = coordinator.coordinate_workflow(
        [
            "create_case",
            "assign_owner",
            "collect_evidence"
        ]
    )

    assert case["status"] == "completed"
    assert len(case["steps"]) == 3


def test_case_assignment():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "analyst-001",
        "soc_analyst"
    )

    assignment = coordinator.assign_task(
        "analyst-001",
        "Investigate phishing incident"
    )

    assert assignment["status"] == "assigned"
    assert assignment["agent_id"] == "analyst-001"


def test_case_investigation_flow():

    coordinator = AutonomousAgentCoordinator()

    workflow = coordinator.coordinate_workflow(
        [
            "triage",
            "evidence_analysis",
            "threat_classification",
            "response"
        ]
    )

    assert workflow["status"] == "completed"

    assert workflow["steps"][0]["status"] == "completed"


def test_case_history_tracking():

    coordinator = AutonomousAgentCoordinator()

    coordinator.coordinate_workflow(
        [
            "case_opened",
            "analysis_started",
            "case_closed"
        ]
    )

    assert len(
        coordinator.workflow_history
    ) == 1


def test_case_platform_status():

    coordinator = AutonomousAgentCoordinator()

    status = coordinator.system_status()

    assert status["status"] == "operational"