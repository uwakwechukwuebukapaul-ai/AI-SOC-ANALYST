from services.agents.autonomous_security_agent_runtime import (
    AutonomousSecurityAgentRuntime
)


def test_register_agent():

    runtime = AutonomousSecurityAgentRuntime()

    agent = runtime.register_agent(
        "agent-001",
        "Threat Hunter Agent",
        "threat_hunting"
    )

    assert agent["agent_id"] == "agent-001"
    assert agent["status"] == "active"


def test_get_agent():

    runtime = AutonomousSecurityAgentRuntime()

    runtime.register_agent(
        "agent-002",
        "Investigation Agent",
        "investigation"
    )

    agent = runtime.get_agent("agent-002")

    assert agent["name"] == "Investigation Agent"


def test_execute_mission():

    runtime = AutonomousSecurityAgentRuntime()

    runtime.register_agent(
        "agent-003",
        "Response Agent",
        "incident_response"
    )

    result = runtime.execute_mission(
        "agent-003",
        "contain malware incident",
        "INC-001"
    )

    assert result["result"] == "completed"


def test_analyze_agent_state():

    runtime = AutonomousSecurityAgentRuntime()

    runtime.register_agent(
        "agent-004",
        "Detection Agent",
        "detection_engineering"
    )

    state = runtime.analyze_agent_state(
        "agent-004"
    )

    assert state["health"] == "healthy"


def test_coordinate_agents():

    runtime = AutonomousSecurityAgentRuntime()

    runtime.register_agent(
        "agent-005",
        "SOC Commander",
        "orchestration"
    )

    result = runtime.coordinate_agents(
        "investigate ransomware activity"
    )

    assert result["coordination_status"] == "initiated"


def test_runtime_history():

    runtime = AutonomousSecurityAgentRuntime()

    runtime.register_agent(
        "agent-006",
        "Threat Intel Agent",
        "intelligence"
    )

    runtime.execute_mission(
        "agent-006",
        "analyze IOC",
        "8.8.8.8"
    )

    history = runtime.history()

    assert len(history) == 1