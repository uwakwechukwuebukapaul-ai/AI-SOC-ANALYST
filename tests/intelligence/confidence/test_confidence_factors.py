from services.intelligence.confidence.confidence_factors import (
    ConfidenceFactorEvaluator,
)


def test_confidence_factors():

    evaluator = ConfidenceFactorEvaluator()


    result = evaluator.evaluate(
        evidence=["ioc"],
        findings=["malware"],
        correlations=["match"],
    )


    assert result["evidence_strength"] > 0
    assert result["finding_quality"] > 0