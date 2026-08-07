"""
Agent Coordination Flow Integration Tests

Validates autonomous security agent collaboration.
"""


from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)


def test_agent_registration_flow():

    coordinator = AutonomousAgentCoordinator()

    detection = coordinator.register_agent(
        "detection-agent",
        "threat_detection"
    )

    investigation = coordinator.register_agent(
        "investigation-agent",
        "investigation"
    )

    assert detection["agent_id"] == "detection-agent"
    assert investigation["agent_type"] == "investigation"

    assert coordinator.get_agent(
        "detection-agent"
    ) is not None


def test_agent_task_assignment():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "response-agent",
        "incident_response"
    )

    result = coordinator.assign_task(
        "response-agent",
        "Contain compromised endpoint"
    )

    assert result["status"] == "assigned"
    assert result["agent_id"] == "response-agent"


def test_agent_workflow_execution():

    coordinator = AutonomousAgentCoordinator()

    workflow = [
        "collect_evidence",
        "analyze_indicators",
        "generate_response"
    ]

    result = coordinator.coordinate_workflow(
        workflow
    )

    assert result["status"] == "completed"
    assert len(result["steps"]) == 3


def test_intelligence_routing():

    coordinator = AutonomousAgentCoordinator()

    result = coordinator.route_intelligence_request(
        "threat_hunting"
    )

    assert result["assigned_agent"] == "hunting_agent"


def test_coordination_history():

    coordinator = AutonomousAgentCoordinator()

    coordinator.coordinate_workflow(
        ["analysis"]
    )

    status = coordinator.system_status()

    assert status["workflows"] == 1