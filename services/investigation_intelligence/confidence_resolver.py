"""
Confidence resolution for unified investigations.
"""

from __future__ import annotations

from typing import Any


class ConfidenceResolver:
    """
    Resolves confidence across multiple intelligence outputs.

    The resolver intentionally uses deterministic logic.
    AI-assisted confidence reasoning can be introduced later
    without changing the public contract.
    """

    def resolve(
        self,
        intelligence: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(intelligence, dict):
            raise TypeError(
                "Intelligence must be a dictionary."
            )

        scores: list[float] = []

        for result in intelligence.values():
            if not isinstance(result, dict):
                continue

            confidence = result.get("confidence")

            if confidence is None:
                confidence = self._derive_confidence(result)

            if confidence is not None:
                try:
                    normalized = float(confidence)
                except (TypeError, ValueError):
                    continue

                scores.append(
                    max(0.0, min(normalized, 1.0))
                )

        if not scores:
            overall = 0.0
        else:
            overall = sum(scores) / len(scores)

        return {
            "score": round(overall, 4),
            "level": self._level(overall),
            "sources": len(scores),
        }

    def _derive_confidence(
        self,
        result: dict[str, Any],
    ) -> float | None:
        """
        Derive a conservative confidence value from
        common intelligence-service signals.
        """

        if result.get("severity") == "critical":
            return 0.95

        if result.get("severity") == "high":
            return 0.85

        if result.get("severity") == "medium":
            return 0.65

        if result.get("matches"):
            return 0.75

        if result.get("techniques"):
            return 0.70

        if result.get("risk_score") is not None:
            try:
                return float(result["risk_score"]) / 100
            except (TypeError, ValueError):
                return None

        return None

    @staticmethod
    def _level(score: float) -> str:
        if score >= 0.85:
            return "high"

        if score >= 0.60:
            return "medium"

        if score > 0:
            return "low"

        return "unknown"