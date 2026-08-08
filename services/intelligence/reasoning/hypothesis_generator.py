"""
Sentinel DNA Hypothesis Generator

Generates possible attack explanations
from correlated intelligence.
"""

from __future__ import annotations

from typing import Any



class HypothesisGenerator:
    """
    Creates investigation hypotheses.

    Future:

    - LLM reasoning
    - attack graph inference
    - MITRE ATT&CK mapping
    """



    def generate(
        self,
        evidence: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Generate possible attack hypotheses.
        """

        hypotheses = []


        for item in evidence:

            value = item.get(
                "value"
            )


            if not value:
                continue


            hypotheses.append(
                {
                    "hypothesis":
                        f"Indicator {value} may be associated with malicious activity",

                    "evidence":
                        item,

                    "type":
                        "security_threat",
                }
            )


        return hypotheses