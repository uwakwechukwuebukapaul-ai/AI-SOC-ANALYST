from services.intelligence.recommendation.recommendation import (
    Recommendation,
)



def test_recommendation():

    result = Recommendation(
        action="Block IOC",
        priority="HIGH",
        reason="Malicious indicator",
    )


    data = result.to_dict()


    assert data["action"] == "Block IOC"

    assert data["priority"] == "HIGH"