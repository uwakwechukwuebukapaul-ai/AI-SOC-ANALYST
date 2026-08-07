from services.risk import RiskIntelligenceEngine


def test_risk_assessment():

    engine = RiskIntelligenceEngine()

    result = engine.assess(
        {
            "risk_score": 70,
            "severity": "high"
        }
    )

    assert result["status"] == "completed"
    assert result["severity"] == "critical"


def test_low_risk_assessment():

    engine = RiskIntelligenceEngine()

    result = engine.assess(
        {
            "risk_score": 10
        }
    )

    assert result["severity"] == "low"