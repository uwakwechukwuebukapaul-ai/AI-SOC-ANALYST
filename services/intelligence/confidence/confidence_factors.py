"""
Sentinel DNA Confidence Factors

Evaluates reliability signals
used by the confidence engine.
"""

from __future__ import annotations

from typing import Any


class ConfidenceFactorEvaluator:
    """
    Calculates confidence contributors.
    """


    def evaluate(
        self,
        evidence: list[Any],
        findings: list[Any],
        correlations: list[Any],
    ) -> dict[str, float]:

        return {

            "evidence_strength":
                self._calculate_factor(
                    evidence
                ),


            "finding_quality":
                self._calculate_factor(
                    findings
                ),


            "correlation_strength":
                self._calculate_factor(
                    correlations
                ),

        }



    def _calculate_factor(
        self,
        values: list[Any],
    ) -> float:

        if not values:

            return 0.0


        score = (
            len(values)
            *
            25
        )


        return min(
            score,
            100.0,
        )