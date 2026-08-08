from services.intelligence.confidence.confidence_score import (
    ConfidenceScore,
)


def test_confidence_score():

    result = ConfidenceScore.calculate(
        90
    )

    assert result.score == 90

    assert result.level == "HIGH"