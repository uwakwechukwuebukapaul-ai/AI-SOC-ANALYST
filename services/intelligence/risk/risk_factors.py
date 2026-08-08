"""
Sentinel DNA Risk Factors

Defines security indicators contributing
to investigation risk.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskFactor:
    """
    Individual risk contributor.
    """

    name: str

    weight: int

    description: str


    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "weight": self.weight,
            "description": self.description,
        }