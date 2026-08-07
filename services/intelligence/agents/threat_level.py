"""
Threat Level

Enterprise threat severity model used throughout Sentinel DNA.

This level is independent from IOC reputation and is intended
for investigation prioritization, dashboards, reporting,
automation, and SOAR workflows.
"""

from __future__ import annotations

from enum import Enum


class ThreatLevel(str, Enum):
    """
    Standardized threat severity.
    """

    INFORMATIONAL = "informational"

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"

    CRITICAL = "critical"

    @property
    def priority(self) -> int:
        """
        Numeric priority.

        Higher value = higher severity.
        """

        return {
            ThreatLevel.INFORMATIONAL: 0,
            ThreatLevel.LOW: 1,
            ThreatLevel.MEDIUM: 2,
            ThreatLevel.HIGH: 3,
            ThreatLevel.CRITICAL: 4,
        }[self]

    @property
    def score(self) -> int:
        """
        Default investigation score.
        """

        return {
            ThreatLevel.INFORMATIONAL: 0,
            ThreatLevel.LOW: 25,
            ThreatLevel.MEDIUM: 50,
            ThreatLevel.HIGH: 75,
            ThreatLevel.CRITICAL: 100,
        }[self]

    @classmethod
    def ordered(cls) -> list["ThreatLevel"]:
        """
        Returns threat levels ordered by severity.
        """

        return [
            cls.INFORMATIONAL,
            cls.LOW,
            cls.MEDIUM,
            cls.HIGH,
            cls.CRITICAL,
        ]

    @classmethod
    def highest(
        cls,
        levels: list["ThreatLevel"],
    ) -> "ThreatLevel":
        """
        Returns the highest severity level.
        """

        if not levels:
            return cls.INFORMATIONAL

        return max(
            levels,
            key=lambda level: level.priority,
        )

    def __str__(self) -> str:
        return self.value