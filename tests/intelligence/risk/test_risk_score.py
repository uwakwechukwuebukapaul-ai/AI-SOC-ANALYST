from services.intelligence.risk.risk_score import (
    RiskScore,
)


def test_risk_score():

    score = RiskScore(
        score=80,
        severity="critical",
        confidence=0.9,
    )


    result = score.to_dict()


    assert result["score"] == 80
    assert result["severity"] == "critical"