from services.investigation.investigation_risk_engine import (
    InvestigationRiskEngine
)


def test_calculate_risk():

    engine = InvestigationRiskEngine()

    result = engine.calculate_risk(
        "INC-001",
        evidence_score=20,
        ioc_score=20,
        threat_score=20
    )

    assert result["risk_score"] == 60
    assert result["risk_level"] == "HIGH"


def test_critical_risk_detection():

    engine = InvestigationRiskEngine()

    result = engine.calculate_risk(
        "INC-002",
        evidence_score=30,
        ioc_score=30,
        threat_score=30
    )

    assert result["risk_level"] == "CRITICAL"


def test_low_risk_detection():

    engine = InvestigationRiskEngine()

    result = engine.calculate_risk(
        "INC-003",
        evidence_score=5
    )

    assert result["risk_level"] == "LOW"


def test_correlation_risk():

    engine = InvestigationRiskEngine()

    result = engine.evaluate_correlation_risk(
        90
    )

    assert result == "CRITICAL"


def test_risk_history():

    engine = InvestigationRiskEngine()

    engine.calculate_risk(
        "INC-004",
        evidence_score=40
    )

    history = engine.get_risk_history()

    assert len(history) == 1


def test_clear_history():

    engine = InvestigationRiskEngine()

    engine.calculate_risk(
        "INC-005",
        evidence_score=40
    )

    engine.clear_history()

    assert len(engine.get_risk_history()) == 0