"""
Sentinel DNA Risk Score

Represents calculated investigation risk.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskScore:
    """
    Enterprise risk score representation.
    """

    score: int

    severity: str

    confidence: float = 0.0


    def to_dict(self) -> dict:
        return {
            "score": self.score,
            "severity": self.severity,
            "confidence": self.confidence,
        }