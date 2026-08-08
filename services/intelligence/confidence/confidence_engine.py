"""
Sentinel DNA Confidence Engine

Combines investigation signals
into final AI confidence score.
"""

from __future__ import annotations

from typing import Any

from .confidence_score import ConfidenceScore
from .confidence_factors import ConfidenceFactorEvaluator



class ConfidenceEngine:

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


        factors = (
            self.factor_evaluator.evaluate(
                evidence=evidence,
                findings=findings,
                correlations=correlations,
            )
        )


        confidence = sum(
            factors.values()
        ) / len(
            factors
        )


        return ConfidenceScore.calculate(
            confidence
        )