from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator
)


def test_register_agent():

    coordinator = AutonomousAgentCoordinator()

    result = coordinator.register_agent(
        "agent-001",
        "detection"
    )

    assert result["agent_id"] == "agent-001"
    assert result["status"] == "registered"


def test_get_agent():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "agent-001",
        "hunting"
    )

    agent = coordinator.get_agent("agent-001")

    assert agent["agent_type"] == "hunting"


def test_assign_task():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "agent-001",
        "response"
    )

    task = coordinator.assign_task(
        "agent-001",
        "contain malware"
    )

    assert task["status"] == "assigned"


def test_coordinate_workflow():

    coordinator = AutonomousAgentCoordinator()

    workflow = coordinator.coordinate_workflow(
        [
            "analyze_alert",
            "map_attack",
            "respond"
        ]
    )

    assert workflow["status"] == "completed"
    assert len(workflow["steps"]) == 3


def test_intelligence_routing():

    coordinator = AutonomousAgentCoordinator()

    result = coordinator.route_intelligence_request(
        "threat_hunting"
    )

    assert result["assigned_agent"] == "hunting_agent"


def test_system_status():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "agent-001",
        "reasoning"
    )

    status = coordinator.system_status()

    assert status["agents"] == 1
    assert status["status"] == "operational"