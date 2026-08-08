from services.intelligence.confidence.confidence_engine import (
    ConfidenceEngine,
)


def test_confidence_engine():

    engine = ConfidenceEngine()


    result = engine.evaluate(
        evidence=[
            "email",
            "ioc",
        ],
        findings=[
            "phishing",
        ],
        correlations=[
            "domain-match",
        ],
    )


    assert result.level in [
        "LOW",
        "MEDIUM",
        "HIGH",
    ]

    assert result.score > 0