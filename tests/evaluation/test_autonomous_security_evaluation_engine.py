from services.evaluation.autonomous_security_evaluation_engine import (
    AutonomousSecurityEvaluationEngine
)


def test_security_event_evaluation():
    engine = AutonomousSecurityEvaluationEngine()

    result = engine.evaluate_security_event(
        {
            "risk_score": 90,
            "confidence": 95
        }
    )

    assert result["evaluation"] == "CRITICAL"
    assert result["accuracy_score"] == "EXCELLENT"


def test_medium_risk_evaluation():
    engine = AutonomousSecurityEvaluationEngine()

    result = engine.evaluate_security_event(
        {
            "risk_score": 40,
            "confidence": 60
        }
    )

    assert result["evaluation"] == "MEDIUM"


def test_low_risk_evaluation():
    engine = AutonomousSecurityEvaluationEngine()

    result = engine.evaluate_security_event(
        {
            "risk_score": 10,
            "confidence": 30
        }
    )

    assert result["evaluation"] == "LOW"


def test_agent_performance_evaluation():
    engine = AutonomousSecurityEvaluationEngine()

    result = engine.evaluate_agent_performance(
        {
            "agent": "Threat Analyst Agent",
            "success_rate": 95
        }
    )

    assert result["performance"] == "OPTIMAL"


def test_evaluation_history():
    engine = AutonomousSecurityEvaluationEngine()

    engine.evaluate_security_event(
        {
            "risk_score": 70,
            "confidence": 80
        }
    )

    history = engine.get_history()

    assert len(history) == 1


def test_clear_history():
    engine = AutonomousSecurityEvaluationEngine()

    engine.evaluate_security_event(
        {
            "risk_score": 70
        }
    )

    engine.clear_history()

    assert len(engine.get_history()) == 0