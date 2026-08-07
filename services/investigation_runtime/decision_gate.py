"""
Decision gate for unified SOC investigations.

The gate provides a deterministic control boundary between analysis
and response automation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class DecisionOutcome(str, Enum):
    REVIEW = "review"
    ESCALATE = "escalate"
    RESPOND = "respond"
    CLOSE = "close"


@dataclass(frozen=True)
class DecisionGate:
    """
    Determines the next operational decision from investigation data.

    The gate supports both:
    - normalized root-level investigation context
    - stage-scoped intelligence results

    Automation remains conservative by default.
    """

    response_threshold: float = 0.85
    escalation_threshold: float = 0.60

    def evaluate(
        self,
        context: dict[str, Any],
    ) -> DecisionOutcome:
        risk_score = self._risk_score(context)
        confidence = self._confidence(context)

        response_authorized = bool(
            context.get("response_authorized", False)
        )

        if (
            response_authorized
            and risk_score >= self.response_threshold
            and confidence >= self.escalation_threshold
        ):
            return DecisionOutcome.RESPOND

        if risk_score >= self.response_threshold:
            return DecisionOutcome.ESCALATE

        if risk_score >= self.escalation_threshold:
            return DecisionOutcome.REVIEW

        return DecisionOutcome.CLOSE

    @classmethod
    def _risk_score(
        cls,
        context: dict[str, Any],
    ) -> float:
        """
        Resolve risk score from the investigation context.

        Root-level values take precedence, followed by the Risk stage.
        """

        value = context.get("risk_score")

        if value is None:
            value = cls._stage_value(
                context,
                "risk",
                "risk_score",
            )

        return cls._normalize_score(value)

    @classmethod
    def _confidence(
        cls,
        context: dict[str, Any],
    ) -> float:
        """
        Resolve confidence from the investigation context.

        Root-level values take precedence, followed by the Risk stage.
        """

        value = context.get("confidence")

        if value is None:
            value = cls._stage_value(
                context,
                "risk",
                "confidence",
            )

        if value is None:
            value = cls._stage_value(
                context,
                "decision",
                "confidence",
            )

        return cls._normalize_score(value)

    @staticmethod
    def _stage_value(
        context: dict[str, Any],
        stage: str,
        key: str,
    ) -> Any:
        stages = context.get("stages", {})

        if not isinstance(stages, dict):
            return None

        stage_data = stages.get(stage)

        if not isinstance(stage_data, dict):
            return None

        return stage_data.get(key)

    @staticmethod
    def _normalize_score(value: Any) -> float:
        try:
            score = float(value)
        except (TypeError, ValueError):
            return 0.0

        if score > 1.0:
            score /= 100.0

        return max(0.0, min(score, 1.0))