from services.agents.autonomous_security_agent_evaluation_engine import (
    AutonomousSecurityAgentEvaluationEngine
)


def test_register_agent():

    engine = AutonomousSecurityAgentEvaluationEngine()

    agent = engine.register_agent(
        "agent-001",
        "Threat Intelligence Agent",
        "threat_intelligence"
    )

    assert agent["role"] == "threat_intelligence"


def test_record_mission_result():

    engine = AutonomousSecurityAgentEvaluationEngine()

    engine.register_agent(
        "agent-002",
        "Detection Agent",
        "detection"
    )

    result = engine.record_mission_result(
        "agent-002",
        True,
        0.9,
        0.85
    )

    assert result["success"] is True


def test_calculate_performance_score():

    engine = AutonomousSecurityAgentEvaluationEngine()

    engine.register_agent(
        "agent-003",
        "Response Agent",
        "response"
    )

    engine.record_mission_result(
        "agent-003",
        True,
        0.9,
        0.9
    )

    score = engine.calculate_performance_score(
        "agent-003"
    )

    assert score["performance_score"] > 0


def test_evaluate_agent_quality():

    engine = AutonomousSecurityAgentEvaluationEngine()

    engine.register_agent(
        "agent-004",
        "SOAR Agent",
        "soar"
    )

    engine.record_mission_result(
        "agent-004",
        True,
        0.95,
        0.95
    )

    result = engine.evaluate_agent_quality(
        "agent-004"
    )

    assert result["quality"] == "excellent"


def test_generate_improvement_recommendation():

    engine = AutonomousSecurityAgentEvaluationEngine()

    engine.register_agent(
        "agent-005",
        "Investigation Agent",
        "investigation"
    )

    engine.record_mission_result(
        "agent-005",
        False,
        0.2,
        0.2
    )

    recommendation = engine.generate_improvement_recommendation(
        "agent-005"
    )

    assert recommendation["recommendation"] == "retrain_agent"


def test_evaluation_history():

    engine = AutonomousSecurityAgentEvaluationEngine()

    engine.register_agent(
        "agent-006",
        "Learning Agent",
        "learning"
    )

    history = engine.evaluation_history()

    assert len(history) > 0