"""
Sentinel DNA Confidence Score

Represents AI investigation confidence.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConfidenceScore:
    """
    Final confidence evaluation result.
    """

    score: float

    level: str

    explanation: str


    @classmethod
    def from_score(
        cls,
        score: float,
    ) -> "ConfidenceScore":

        score = max(
            0.0,
            min(
                100.0,
                score,
            ),
        )


        if score >= 80:

            level = "HIGH"


        elif score >= 50:

            level = "MEDIUM"


        else:

            level = "LOW"



        return cls(
            score=score,
            level=level,
            explanation=(
                f"AI confidence calculated at "
                f"{score:.2f}%"
            ),
        )


    def to_dict(self) -> dict:

        return {
            "score": self.score,
            "level": self.level,
            "explanation": self.explanation,
        }