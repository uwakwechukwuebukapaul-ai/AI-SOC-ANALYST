"""
Sentinel DNA Risk Engine

Calculates investigation risk
from security factors.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.risk.risk_score import (
    RiskScore,
)

from services.intelligence.risk.risk_factors import (
    RiskFactor,
)


class RiskEngine:
    """
    Enterprise risk calculation engine.
    """


    def __init__(self):

        self.default_factors = [
            RiskFactor(
                name="malicious_indicator",
                weight=40,
                description=(
                    "Known malicious IOC detected"
                ),
            ),

            RiskFactor(
                name="high_severity_alert",
                weight=30,
                description=(
                    "High severity security alert"
                ),
            ),

            RiskFactor(
                name="external_threat",
                weight=20,
                description=(
                    "External threat activity"
                ),
            ),
        ]


    def calculate(
        self,
        findings: list[dict[str, Any]],
    ) -> RiskScore:
        """
        Calculate risk score.
        """

        total = 0

        matched = []


        for finding in findings:

            if not isinstance(
                finding,
                dict,
            ):
                continue


            text = str(
                finding
            ).lower()


            if "malicious" in text:

                total += 40

                matched.append(
                    "malicious_indicator"
                )


            if "high" in text:

                total += 30

                matched.append(
                    "high_severity_alert"
                )


            if "external" in text:

                total += 20

                matched.append(
                    "external_threat"
                )


        if total >= 80:

            severity = "critical"

        elif total >= 50:

            severity = "high"

        elif total >= 25:

            severity = "medium"

        else:

            severity = "low"


        confidence = min(
            total / 100,
            1.0,
        )


        return RiskScore(
            score=total,
            severity=severity,
            confidence=confidence,
        )


    def analyze(
        self,
        artifacts: list[dict[str, Any]],
    ) -> RiskScore:

        return self.calculate(
            artifacts
        )