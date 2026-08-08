"""
Recommendation Model

Represents an AI-generated SOC action.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Recommendation:
    """
    Analyst recommendation result.
    """

    action: str

    priority: str

    reason: str


    def to_dict(self) -> dict:

        return {
            "action": self.action,
            "priority": self.priority,
            "reason": self.reason,
        }