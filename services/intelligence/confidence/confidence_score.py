"""
Confidence Score Model

Represents AI investigation confidence.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConfidenceScore:
    """
    Investigation confidence result.
    """

    score: float

    level: str

    explanation: str


    @classmethod
    def calculate(
        cls,
        value: float,
    ) -> "ConfidenceScore":

        value = max(
            0,
            min(
                100,
                value,
            ),
        )

        if value >= 80:
            level = "HIGH"

        elif value >= 50:
            level = "MEDIUM"

        else:
            level = "LOW"


        return cls(
            score=value,
            level=level,
            explanation=(
                f"Confidence calculated at {value}%"
            ),
        )


    def to_dict(self) -> dict:

        return {
            "score": self.score,
            "level": self.level,
            "explanation": self.explanation,
        }