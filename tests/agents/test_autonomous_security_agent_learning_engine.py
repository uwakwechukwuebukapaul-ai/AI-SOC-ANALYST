from services.agents.autonomous_security_agent_learning_engine import (
    AutonomousSecurityAgentLearningEngine,
)


def test_register_agent():

    engine = AutonomousSecurityAgentLearningEngine()

    agent = engine.register_agent(
        "agent-001",
        ["threat_detection", "incident_response"],
    )

    assert agent["agent_id"] == "agent-001"
    assert "threat_detection" in agent["capabilities"]


def test_record_learning_event():

    engine = AutonomousSecurityAgentLearningEngine()

    engine.register_agent("agent-001")

    learning = engine.record_learning_event(
        agent_id="agent-001",
        event_type="incident_analysis",
        observation="Detected ransomware behavior",
        result="success",
        improvement_area="behavior_detection",
    )

    assert learning["agent_id"] == "agent-001"
    assert learning["result"] == "success"


def test_analyze_learning_pattern():

    engine = AutonomousSecurityAgentLearningEngine()

    engine.register_agent("agent-001")

    engine.record_learning_event(
        "agent-001",
        "response",
        "Blocked malicious process",
        "success",
        "automation",
    )

    analysis = engine.analyze_learning_pattern("agent-001")

    assert analysis["learning_events"] == 1
    assert analysis["successful_learning"] == 1
    assert analysis["status"] == "analyzed"


def test_generate_learning_strategy():

    engine = AutonomousSecurityAgentLearningEngine()

    engine.register_agent("agent-001")

    engine.record_learning_event(
        "agent-001",
        "investigation",
        "Failed IOC classification",
        "failure",
        "classification",
    )

    result = engine.generate_learning_strategy(
        "agent-001"
    )

    assert "failed scenarios" in result["strategy"]


def test_evaluate_agent_growth():

    engine = AutonomousSecurityAgentLearningEngine()

    engine.register_agent("agent-001")

    engine.record_learning_event(
        "agent-001",
        "learning",
        "New detection pattern learned",
        "success",
    )

    growth = engine.evaluate_agent_growth(
        "agent-001"
    )

    assert growth["learning_score"] == 1
    assert growth["growth_level"] == "initial"


def test_learning_history():

    engine = AutonomousSecurityAgentLearningEngine()

    engine.register_agent("agent-001")

    engine.record_learning_event(
        "agent-001",
        "memory_update",
        "Stored threat intelligence",
        "success",
    )

    history = engine.learning_history()

    assert len(history) == 1