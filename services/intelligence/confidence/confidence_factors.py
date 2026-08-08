"""
Confidence Factor Evaluation

Measures investigation reliability.
"""

from __future__ import annotations

from typing import Any


class ConfidenceFactorEvaluator:
    """
    Calculates confidence factors.
    """


    def evaluate(
        self,
        evidence: list[Any],
        findings: list[Any],
        correlations: list[Any],
    ) -> dict[str, float]:

        return {

            "evidence_strength":
                self._score_length(
                    evidence
                ),

            "finding_quality":
                self._score_length(
                    findings
                ),

            "correlation_quality":
                self._score_length(
                    correlations
                ),

        }


    def _score_length(
        self,
        items: list[Any],
    ) -> float:

        if not items:
            return 0.0


        score = len(items) * 25

        return min(
            score,
            100.0,
        )