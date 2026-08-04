from services.agents.autonomous_agent_runtime import AutonomousAgentRuntime


def test_register_agent():

    runtime = AutonomousAgentRuntime()

    agent = runtime.register_agent(
        "agent-001",
        "detection_agent"
    )

    assert agent["agent_id"] == "agent-001"
    assert agent["status"] == "registered"



def test_start_agent():

    runtime = AutonomousAgentRuntime()

    runtime.register_agent(
        "agent-001",
        "investigation_agent"
    )

    result = runtime.start_agent("agent-001")

    assert result["status"] == "running"



def test_execute_task():

    runtime = AutonomousAgentRuntime()

    runtime.register_agent(
        "agent-001",
        "response_agent"
    )

    result = runtime.execute_task(
        "agent-001",
        "analyze_alert"
    )

    assert result["status"] == "completed"
    assert result["task"] == "analyze_alert"



def test_agent_health():

    runtime = AutonomousAgentRuntime()

    runtime.register_agent(
        "agent-001",
        "hunting_agent"
    )

    health = runtime.agent_health("agent-001")

    assert health["health"] == "healthy"



def test_execution_history():

    runtime = AutonomousAgentRuntime()

    runtime.register_agent(
        "agent-001",
        "copilot_agent"
    )

    runtime.execute_task(
        "agent-001",
        "summarize_incident"
    )

    history = runtime.runtime_history()

    assert len(history) == 1



def test_clear_history():

    runtime = AutonomousAgentRuntime()

    runtime.clear_history()

    assert runtime.runtime_history() == []