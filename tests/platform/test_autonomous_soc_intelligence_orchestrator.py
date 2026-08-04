from services.platform.autonomous_soc_intelligence_orchestrator import (
    AutonomousSOCIntelligenceOrchestrator
)


def test_process_security_event():

    engine = AutonomousSOCIntelligenceOrchestrator()

    result = engine.process_security_event(
        {
            "type": "malware",
            "severity": "high"
        }
    )

    assert result["risk"]["level"] == "high"
    assert "decision" in result


def test_critical_event_response():

    engine = AutonomousSOCIntelligenceOrchestrator()

    result = engine.process_security_event(
        {
            "type": "ransomware",
            "severity": "critical"
        }
    )

    assert result["response"]["priority"] == "immediate"


def test_low_risk_event():

    engine = AutonomousSOCIntelligenceOrchestrator()

    result = engine.process_security_event(
        {
            "type": "login anomaly",
            "severity": "low"
        }
    )

    assert result["risk"]["score"] == 20


def test_system_status():

    engine = AutonomousSOCIntelligenceOrchestrator()

    status = engine.get_system_status()

    assert status["status"] == "healthy"
    assert "soc_brain" in status["components"]


def test_history_tracking():

    engine = AutonomousSOCIntelligenceOrchestrator()

    engine.process_security_event(
        {
            "type": "phishing",
            "severity": "medium"
        }
    )

    history = engine.get_history()

    assert len(history) == 1


def test_clear_history():

    engine = AutonomousSOCIntelligenceOrchestrator()

    engine.process_security_event(
        {
            "type": "malware",
            "severity": "high"
        }
    )

    result = engine.clear_history()

    assert result["status"] == "cleared"
    assert len(engine.get_history()) == 0