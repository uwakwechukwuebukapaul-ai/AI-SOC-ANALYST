from services.learning.autonomous_learning_engine import (
    AutonomousLearningEngine
)


def test_store_feedback():
    engine = AutonomousLearningEngine()

    result = engine.store_feedback(
        "INC001",
        "resolved",
        "IOC matching improved"
    )

    assert result["investigation_id"] == "INC001"
    assert len(engine.feedback_history) == 1


def test_learning_pattern_generation():
    engine = AutonomousLearningEngine()

    engine.store_feedback(
        "INC002",
        "failed",
        "Improve correlation accuracy"
    )

    assert len(engine.learning_patterns) == 1


def test_agent_performance():
    engine = AutonomousLearningEngine()

    result = engine.analyze_agent_performance(
        "threat_agent",
        True,
        0.95
    )

    assert result["success_rate"] == 1
    assert result["average_confidence"] == 0.95


def test_multiple_agent_executions():
    engine = AutonomousLearningEngine()

    engine.analyze_agent_performance(
        "investigator",
        True,
        0.9
    )

    engine.analyze_agent_performance(
        "investigator",
        False,
        0.5
    )

    result = engine.get_agent_performance(
        "investigator"
    )

    assert result["success_rate"] == 0.5


def test_improvement_recommendation():
    engine = AutonomousLearningEngine()

    result = engine.recommend_improvement(
        {
            "false_positive": True
        }
    )

    assert "Improve detection precision" in result


def test_learning_history():
    engine = AutonomousLearningEngine()

    history = engine.get_learning_history()

    assert "feedback" in history
    assert "patterns" in history
    assert "agents" in history