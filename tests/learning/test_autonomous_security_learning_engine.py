from services.learning.autonomous_security_learning_engine import (
    AutonomousSecurityLearningEngine
)


def test_learn_from_incident():

    engine = AutonomousSecurityLearningEngine()

    result = engine.learn_from_incident(
        "ransomware attack",
        "endpoint isolated"
    )

    assert result["type"] == "incident_learning"


def test_analyze_feedback():

    engine = AutonomousSecurityLearningEngine()

    result = engine.analyze_feedback(
        "analyst approved automated containment"
    )

    assert result["type"] == "analyst_feedback"
    assert result["improvement"] is True


def test_threat_pattern_learning():

    engine = AutonomousSecurityLearningEngine()

    result = engine.improve_threat_pattern(
        "credential dumping",
        "LSASS access behavior"
    )

    assert result["type"] == "pattern_learning"


def test_response_optimization():

    engine = AutonomousSecurityLearningEngine()

    result = engine.optimize_response(
        "manual investigation",
        "automated investigation workflow"
    )

    assert result["type"] == "response_optimization"


def test_learning_confidence():

    engine = AutonomousSecurityLearningEngine()

    learning = engine.learn_from_incident(
        "phishing",
        "blocked"
    )

    result = engine.calculate_learning_confidence(
        learning["id"]
    )

    assert result["level"] == "high"


def test_learning_history():

    engine = AutonomousSecurityLearningEngine()

    engine.learn_from_incident(
        "malware",
        "removed"
    )

    assert len(
        engine.get_learning_history()
    ) == 1