"""
Sentinel DNA Recommendation Intelligence

Transforms investigation intelligence
into recommended SOC actions.
"""

from .recommendation import Recommendation
from .recommendation_rules import RecommendationRuleEngine
from .recommendation_engine import RecommendationEngine


__all__ = [
    "Recommendation",
    "RecommendationRuleEngine",
    "RecommendationEngine",
]