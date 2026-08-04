from services.reflection.autonomous_security_reflection_engine import (
    AutonomousSecurityReflectionEngine
)


def test_incident_reflection():

    engine = AutonomousSecurityReflectionEngine()

    result = engine.reflect_on_incident({
        "id": "INC001",
        "risk": "CRITICAL"
    })

    assert result["confidence"] == 0.9
    assert "containment" in result["analysis"]


def test_response_analysis():

    engine = AutonomousSecurityReflectionEngine()

    result = engine.analyze_response({
        "success": True
    })

    assert result["confidence"] == 0.9
    assert "effectively" in result["insight"]


def test_failed_response_analysis():

    engine = AutonomousSecurityReflectionEngine()

    result = engine.analyze_response({
        "success": False
    })

    assert result["confidence"] == 0.6


def test_improvement_plan():

    engine = AutonomousSecurityReflectionEngine()

    result = engine.generate_improvement_plan({
        "risk": "HIGH"
    })

    assert result["priority"] == "HIGH"
    assert len(result["recommendations"]) == 3


def test_reflection_history():

    engine = AutonomousSecurityReflectionEngine()

    engine.reflect_on_incident({
        "risk": "LOW"
    })

    history = engine.get_reflection_history()

    assert len(history) == 1


def test_clear_history():

    engine = AutonomousSecurityReflectionEngine()

    engine.reflect_on_incident({
        "risk": "MEDIUM"
    })

    result = engine.clear_history()

    assert result["status"] == "cleared"
    assert len(engine.get_reflection_history()) == 0