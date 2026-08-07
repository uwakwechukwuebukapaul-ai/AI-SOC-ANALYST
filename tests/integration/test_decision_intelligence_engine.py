from services.decision_intelligence import (
    DecisionIntelligenceEngine
)



def test_security_decision():

    engine = DecisionIntelligenceEngine()


    result = engine.evaluate(

        {
            "case": "INC-001"
        },

        {
            "risk_score": 90
        },

        {
            "matches": [
                "credential_attack"
            ],
            "threat_level": "high"
        }

    )


    assert result["type"] == (
        "security_decision"
    )


    assert result["confidence"] == 100



def test_decision_history():

    engine = DecisionIntelligenceEngine()

    engine.evaluate(
        {},
        {},
        {}
    )

    assert len(
        engine.history()
    ) == 1