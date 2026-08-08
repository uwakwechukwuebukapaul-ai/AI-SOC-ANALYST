from services.intelligence.reasoning.reasoning_engine import (
    ReasoningEngine,
)



def test_reasoning_engine():


    engine = ReasoningEngine()


    evidence = [

        {
            "type": "ioc",
            "value": "malicious-domain.xyz",
        },

        {
            "type": "threat",
            "value": "phishing",
        },

    ]



    result = engine.analyze(
        evidence
    )


    assert (
        result["reasoning_status"]
        ==
        "completed"
    )


    assert (
        len(
            result["hypotheses"]
        )
        ==
        2
    )


    assert (
        result["confidence"]
        ==
        40
    )