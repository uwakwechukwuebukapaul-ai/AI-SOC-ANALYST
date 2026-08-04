from services.risk.autonomous_security_risk_intelligence_engine import (
    AutonomousSecurityRiskIntelligenceEngine
)


def test_register_asset():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    asset = engine.register_asset(
        "SERVER-001",
        "database",
        5
    )

    assert asset["asset_id"] == "SERVER-001"


def test_analyze_asset_risk():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    engine.register_asset(
        "SERVER-001",
        "database",
        5
    )

    result = engine.analyze_asset_risk(
        "SERVER-001",
        5,
        4
    )

    assert result["risk_score"] > 0


def test_analyze_threat_risk():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    result = engine.analyze_threat_risk(
        "Ransomware",
        10,
        9
    )

    assert result["risk_level"] == "CRITICAL"


def test_identity_risk():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    result = engine.analyze_identity_risk(
        "admin",
        5,
        5
    )

    assert result["identity_risk_score"] > 0


def test_generate_risk_report():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    engine.analyze_threat_risk(
        "Phishing",
        8,
        8
    )

    report = engine.generate_risk_report()

    assert report["total_records"] == 1


def test_risk_history():

    engine = AutonomousSecurityRiskIntelligenceEngine()

    engine.analyze_threat_risk(
        "Malware",
        7,
        7
    )

    history = engine.risk_history_records()

    assert len(history) == 1