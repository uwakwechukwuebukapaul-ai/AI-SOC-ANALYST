"""
Sentinel DNA Recommendation Engine

Produces AI-assisted SOC recommendations.
"""

from __future__ import annotations

from typing import Any

from .recommendation import Recommendation

from .recommendation_rules import (
    RecommendationRuleEngine,
)



class RecommendationEngine:
    """
    Enterprise recommendation generator.
    """


    def __init__(self):

        self.rules = (
            RecommendationRuleEngine()
        )


    def generate(
        self,
        risk_level: str,
        findings: list[Any],
    ) -> list[Recommendation]:


        raw = self.rules.generate(
            risk_level=risk_level,
            findings=findings,
        )


        return [

            Recommendation(
                action=item["action"],
                priority=item["priority"],
                reason=item["reason"],
            )

            for item in raw

        ]