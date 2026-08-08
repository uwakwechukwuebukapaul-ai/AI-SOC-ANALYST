from services.intelligence.recommendation.recommendation_engine import (
    RecommendationEngine,
)



def test_recommendation_engine():

    engine = RecommendationEngine()


    result = engine.generate(
        risk_level="HIGH",
        findings=[
            {
                "type": "phishing"
            }
        ],
    )


    assert len(result) > 0

    assert result[0].priority == "HIGH"