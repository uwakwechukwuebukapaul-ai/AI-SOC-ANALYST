from services.intelligence.recommendation.recommendation_rules import (
    RecommendationRuleEngine,
)



def test_recommendation_rules():

    engine = RecommendationRuleEngine()


    result = engine.generate(
        risk_level="HIGH",
        findings=[
            "malware"
        ],
    )


    assert len(result) > 0

    assert result[0]["priority"] == "HIGH"