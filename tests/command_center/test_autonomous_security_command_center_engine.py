from services.command_center.autonomous_security_command_center_engine import (
    AutonomousSecurityCommandCenterEngine
)


def test_register_engine():
    engine = AutonomousSecurityCommandCenterEngine()

    result = engine.register_engine(
        "Threat Intelligence Engine",
        "intelligence",
        ["IOC analysis", "Threat actor tracking"]
    )

    assert result["status"] == "active"
    assert result["name"] == "Threat Intelligence Engine"


def test_analyze_security_state():
    engine = AutonomousSecurityCommandCenterEngine()

    result = engine.analyze_security_state(
        {
            "risk_score": 85,
            "active_incidents": 3,
            "threats": 10
        }
    )

    assert result["security_posture"] == "critical"
    assert result["risk_score"] == 85


def test_coordinate_security_operation():
    engine = AutonomousSecurityCommandCenterEngine()

    result = engine.coordinate_security_operation(
        "incident_response",
        "SOAR Engine",
        "Contain ransomware activity"
    )

    assert result["status"] == "initiated"
    assert result["target_engine"] == "SOAR Engine"


def test_generate_autonomous_strategy():
    engine = AutonomousSecurityCommandCenterEngine()

    result = engine.generate_autonomous_strategy(
        {
            "security_posture": "high"
        }
    )

    assert "recommended_actions" in result
    assert result["confidence"] > 0


def test_engine_registry():
    engine = AutonomousSecurityCommandCenterEngine()

    engine.register_engine(
        "Risk Engine",
        "risk",
        ["risk scoring"]
    )

    assert "Risk Engine" in engine.engines


def test_command_history():
    engine = AutonomousSecurityCommandCenterEngine()

    engine.register_engine(
        "Detection Engine",
        "detection",
        ["rule optimization"]
    )

    history = engine.get_command_history()

    assert len(history) > 0