"""
Sentinel DNA Analyst Summary Generator

Creates SOC analyst focused summaries.
"""

from __future__ import annotations

from typing import Any



class AnalystSummaryGenerator:
    """
    Generates analyst investigation summary.
    """

    def generate(
        self,
        intelligence: dict[str, Any],
    ) -> str:
        """
        Generate concise SOC summary.
        """

        correlation = intelligence.get(
            "correlation",
            {},
        )


        reasoning = intelligence.get(
            "reasoning",
            {},
        )


        findings = correlation.get(
            "correlated_findings",
            0,
        )


        confidence = reasoning.get(
            "confidence",
            0,
        )


        return (
            f"Investigation identified "
            f"{findings} correlated findings "
            f"with {confidence}% confidence."
        )