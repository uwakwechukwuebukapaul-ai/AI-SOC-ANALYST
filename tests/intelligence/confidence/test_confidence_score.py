from services.intelligence.confidence.confidence_score import (
    ConfidenceScore,
)



def test_confidence_score():

    result = ConfidenceScore.from_score(
        90
    )


    assert result.score == 90

    assert result.level == "HIGH"

    assert "90" in result.explanation