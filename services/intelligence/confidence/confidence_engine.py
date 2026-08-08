"""
Sentinel DNA Confidence Engine

Combines investigation signals
into explainable AI confidence.
"""

from __future__ import annotations

from typing import Any


from services.intelligence.confidence.confidence_score import (
    ConfidenceScore,
)


from services.intelligence.confidence.confidence_factors import (
    ConfidenceFactorEvaluator,
)



class ConfidenceEngine:
    """
    Enterprise confidence calculation engine.
    """


    def __init__(self):

        self.factor_evaluator = (
            ConfidenceFactorEvaluator()
        )



    def evaluate(
        self,
        evidence: list[Any],
        findings: list[Any],
        correlations: list[Any],
    ) -> ConfidenceScore:
        """
        Generate confidence score.
        """


        factors = (
            self.factor_evaluator.evaluate(
                evidence=evidence,
                findings=findings,
                correlations=correlations,
            )
        )


        if not factors:

            return ConfidenceScore.from_score(
                0
            )


        confidence = (
            sum(
                factors.values()
            )
            /
            len(factors)
        )


        return ConfidenceScore.from_score(
            confidence
        )