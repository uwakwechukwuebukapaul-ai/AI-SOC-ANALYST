"""
Sentinel DNA
Agent Reasoning Intelligence Layer

Provides autonomous reasoning capabilities for SOC agents.

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


def utc_now():
    return datetime.now(timezone.utc)


@dataclass
class ReasoningDecision:
    """
    Represents an AI agent decision.
    """

    action: str

    explanation: str

    confidence: float

    priority: str = "MEDIUM"

    created_at: datetime = field(
        default_factory=utc_now
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "action": self.action,
            "explanation": self.explanation,
            "confidence": self.confidence,
            "priority": self.priority,
            "created_at": self.created_at.isoformat(),
        }


class AgentReasoningEngine:
    """
    Enterprise reasoning engine for Sentinel DNA agents.

    Responsible for:
    - context evaluation
    - decision generation
    - confidence scoring
    - reasoning explanation
    """

    def __init__(self):
        self.reasoning_history: List[Dict[str, Any]] = []


    def evaluate_context(
        self,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze investigation context.
        """

        risk_score = context.get(
            "risk_score",
            0
        )

        severity = context.get(
            "severity",
            "Low"
        )

        indicators = len(
            context.get(
                "iocs",
                []
            )
        )


        assessment = {

            "risk_level": self._calculate_risk_level(
                risk_score
            ),

            "severity": severity,

            "ioc_count": indicators,

            "requires_action": (
                risk_score >= 70
                or severity in [
                    "High",
                    "Critical"
                ]
            ),

            "timestamp": utc_now().isoformat(),
        }


        return assessment



    def generate_decision(
        self,
        context: Dict[str, Any]
    ) -> ReasoningDecision:
        """
        Generate autonomous agent decision.
        """

        evaluation = self.evaluate_context(
            context
        )


        if evaluation["requires_action"]:

            decision = ReasoningDecision(

                action="INITIATE_RESPONSE",

                explanation=(
                    "High risk indicators detected. "
                    "Investigation requires response workflow."
                ),

                confidence=0.90,

                priority="HIGH",
            )

        else:

            decision = ReasoningDecision(

                action="CONTINUE_ANALYSIS",

                explanation=(
                    "Risk level is currently manageable. "
                    "Additional analysis is recommended."
                ),

                confidence=0.75,

                priority="MEDIUM",
            )


        self.reasoning_history.append(
            decision.to_dict()
        )


        return decision



    def calculate_confidence(
        self,
        evidence_count: int,
        intelligence_count: int,
    ) -> float:
        """
        Calculate reasoning confidence.
        """

        score = (
            evidence_count * 0.1
            +
            intelligence_count * 0.15
        )


        return min(
            round(score, 2),
            1.0
        )



    def explain_reasoning(
        self,
        decision: ReasoningDecision
    ) -> str:
        """
        Human readable explanation.
        """

        return (
            f"Decision: {decision.action}. "
            f"Reason: {decision.explanation} "
            f"Confidence: {decision.confidence}"
        )



    def get_history(
        self
    ) -> List[Dict[str, Any]]:
        return self.reasoning_history



    def clear_history(
        self
    ) -> None:

        self.reasoning_history.clear()



    def _calculate_risk_level(
        self,
        score: int
    ) -> str:

        if score >= 90:
            return "CRITICAL"

        if score >= 70:
            return "HIGH"

        if score >= 40:
            return "MEDIUM"

        return "LOW"