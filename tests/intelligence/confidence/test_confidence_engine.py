from services.intelligence.confidence.confidence_engine import (
    ConfidenceEngine,
)



def test_confidence_engine():


    engine = ConfidenceEngine()


    result = engine.evaluate(

        evidence=[
            {
                "type": "ioc",
            },

            {
                "type": "email",
            },
        ],


        findings=[

            {
                "type": "malicious",
            }

        ],


        correlations=[

            {
                "match": True,
            }

        ],
    )


    assert result.score > 0


    assert result.level in [

        "LOW",
        "MEDIUM",
        "HIGH",

    ]