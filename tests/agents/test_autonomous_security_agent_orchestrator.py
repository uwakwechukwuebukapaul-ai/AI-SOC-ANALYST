from services.agents.autonomous_security_agent_orchestrator import (
    AutonomousSecurityAgentOrchestrator
)


def test_register_agent():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    agent = orchestrator.register_agent(
        "agent-001",
        "Threat Intelligence Agent",
        "threat_intelligence",
        5
    )

    assert agent["agent_id"] == "agent-001"


def test_list_agents():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    orchestrator.register_agent(
        "agent-002",
        "Investigation Agent",
        "investigation"
    )

    agents = orchestrator.list_agents()

    assert len(agents) == 1


def test_select_agent():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    orchestrator.register_agent(
        "agent-003",
        "Hunter Agent",
        "threat_hunting",
        10
    )

    agent = orchestrator.select_agent(
        "threat_hunting"
    )

    assert agent["name"] == "Hunter Agent"


def test_create_mission():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    orchestrator.register_agent(
        "agent-004",
        "Response Agent",
        "incident_response"
    )

    mission = orchestrator.create_mission(
        "MISSION-001",
        "Contain ransomware incident",
        "incident_response"
    )

    assert mission["status"] == "assigned"


def test_execute_mission():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    orchestrator.register_agent(
        "agent-005",
        "Detection Agent",
        "detection"
    )

    orchestrator.create_mission(
        "MISSION-002",
        "Improve detection coverage",
        "detection"
    )

    result = orchestrator.execute_mission(
        "MISSION-002"
    )

    assert result["status"] == "completed"


def test_orchestration_history():

    orchestrator = AutonomousSecurityAgentOrchestrator()

    orchestrator.create_mission(
        "MISSION-003",
        "Security assessment",
        "risk"
    )

    history = orchestrator.orchestration_history()

    assert len(history) == 1