from services.intelligence.investigation.investigation_intelligence import (
    InvestigationIntelligence,
)



def test_investigation_intelligence():


    engine = InvestigationIntelligence()


    artifacts = [

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
        artifacts
    )


    assert (
        result["status"]
        ==
        "completed"
    )


    assert (
        result["correlation"]["status"]
        ==
        "completed"
    )


    assert (
        result["reasoning"]["reasoning_status"]
        ==
        "completed"
    )