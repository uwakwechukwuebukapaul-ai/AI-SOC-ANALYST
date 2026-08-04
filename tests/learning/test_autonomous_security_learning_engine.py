from services.learning.autonomous_security_learning_engine import (
    AutonomousSecurityLearningEngine
)


def test_record_security_lesson():

    engine = AutonomousSecurityLearningEngine()

    result = engine.record_security_lesson(
        "phishing",
        "blocked",
        "Improve phishing detection"
    )

    assert result["incident_type"] == "phishing"



def test_analyze_learning_pattern():

    engine = AutonomousSecurityLearningEngine()

    engine.record_security_lesson(
        "malware",
        "blocked",
        "Improve malware response"
    )

    result = engine.analyze_learning_pattern()

    assert result["total_lessons"] == 1



def test_update_agent_knowledge():

    engine = AutonomousSecurityLearningEngine()

    result = engine.update_agent_knowledge(
        "investigation_agent",
        "new malware behaviour"
    )

    assert result["knowledge_count"] == 1



def test_generate_learning_recommendation():

    engine = AutonomousSecurityLearningEngine()

    result = engine.generate_learning_recommendation(
        {
            "total_lessons": 5
        }
    )

    assert len(
        result["recommendations"]
    ) > 0



def test_learning_confidence_score():

    engine = AutonomousSecurityLearningEngine()

    result = engine.calculate_learning_confidence(
        8,
        10
    )

    assert result["confidence"] == 0.8



def test_learning_history():

    engine = AutonomousSecurityLearningEngine()

    engine.record_security_lesson(
        "ransomware",
        "contained",
        "Improve isolation"
    )

    history = engine.get_history()

    assert len(history) > 0