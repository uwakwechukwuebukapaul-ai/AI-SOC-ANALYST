from services.intelligence.risk.risk_engine import (
    RiskEngine,
)


def test_risk_engine():

    engine = RiskEngine()


    result = engine.analyze(
        [
            {
                "indicator": "malicious-domain.xyz",
                "severity": "high",
            }
        ]
    )


    assert result.score > 0

    assert result.severity in [
        "medium",
        "high",
        "critical",
    ]