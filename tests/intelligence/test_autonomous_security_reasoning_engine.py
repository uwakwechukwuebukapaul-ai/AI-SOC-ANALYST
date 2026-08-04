from services.intelligence.autonomous_security_reasoning_engine import (
    AutonomousSecurityReasoningEngine
)


def test_security_reasoning_analysis():
    engine = AutonomousSecurityReasoningEngine()

    result = engine.analyze_security_context({
        "risk_score": 90,
        "threats": ["malware"],
        "evidence": ["file_hash"]
    })

    assert result["severity"] == "CRITICAL"
    assert result["decision"] == "Immediate containment recommended"


def test_high_risk_reasoning():
    engine = AutonomousSecurityReasoningEngine()

    result = engine.analyze_security_context({
        "risk_score": 60,
        "threats": ["suspicious_login"]
    })

    assert result["severity"] == "HIGH"


def test_low_risk_reasoning():
    engine = AutonomousSecurityReasoningEngine()

    result = engine.analyze_security_context({
        "risk_score": 10
    })

    assert result["severity"] == "LOW"


def test_generate_recommendation():
    engine = AutonomousSecurityReasoningEngine()

    recommendations = engine.generate_recommendation({
        "severity": "CRITICAL"
    })

    assert "Contain affected assets" in recommendations


def test_threat_intelligence_correlation():
    engine = AutonomousSecurityReasoningEngine()

    result = engine.correlate_threat_intelligence([
        {
            "value": "8.8.8.8",
            "malicious": True
        }
    ])

    assert len(result) == 1
    assert result[0]["confidence"] == "HIGH"


def test_reasoning_history():
    engine = AutonomousSecurityReasoningEngine()

    engine.analyze_security_context({
        "risk_score": 70
    })

    assert len(engine.get_reasoning_history()) == 1

    engine.clear_history()

    assert len(engine.get_reasoning_history()) == 0