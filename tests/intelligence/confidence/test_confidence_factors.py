from services.intelligence.confidence.confidence_factors import (
    ConfidenceFactorEvaluator,
)



def test_confidence_factor_evaluator():

    evaluator = (
        ConfidenceFactorEvaluator()
    )


    result = evaluator.evaluate(
        evidence=[
            "IOC",
        ],

        findings=[
            "phishing",
        ],

        correlations=[
            "domain match",
        ],
    )


    assert (
        result["evidence_strength"]
        > 0
    )


    assert (
        result["finding_quality"]
        > 0
    )