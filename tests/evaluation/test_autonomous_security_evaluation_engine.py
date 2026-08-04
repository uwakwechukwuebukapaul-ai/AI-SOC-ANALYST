from services.evaluation.autonomous_security_evaluation_engine import (
    AutonomousSecurityEvaluationEngine
)


def test_evaluate_agent_performance():

    engine = AutonomousSecurityEvaluationEngine()

    result = engine.evaluate_agent_performance(
        "investigation_agent",
        95
    )

    assert result["performance_score"] == 95


def test_detection_accuracy_score():

    engine = AutonomousSecurityEvaluationEngine()

    result = engine.detection_accuracy_score(
        90,
        100
    )

    assert result["score"] == 90


def test_decision_quality_score():

    engine = AutonomousSecurityEvaluationEngine()

    result = engine.decision_quality_score(
        80,
        100
    )

    assert result["score"] == 80


def test_investigation_quality_score():

    engine = AutonomousSecurityEvaluationEngine()

    result = engine.investigation_quality_score(
        90,
        80
    )

    assert result["score"] == 85


def test_generate_evaluation_report():

    engine = AutonomousSecurityEvaluationEngine()

    result = engine.generate_evaluation_report(
        "Sentinel DNA",
        {
            "accuracy": 95
        }
    )

    assert result["system"] == "Sentinel DNA"


def test_evaluation_history():

    engine = AutonomousSecurityEvaluationEngine()

    engine.evaluate_agent_performance(
        "agent",
        90
    )

    history = engine.get_history()

    assert len(history) == 1