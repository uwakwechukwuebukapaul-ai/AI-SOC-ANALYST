"""
Sentinel DNA Severity Engine
"""


class SeverityEngine:


    def calculate(
        self,
        findings: list[dict],
    ) -> tuple[str, float]:

        score = 0


        for finding in findings:

            severity = finding.get(
                "severity",
                "low"
            )


            if severity == "critical":
                score += 40

            elif severity == "high":
                score += 25

            elif severity == "medium":
                score += 10

            else:
                score += 5


        if score >= 70:
            level = "CRITICAL"

        elif score >= 40:
            level = "HIGH"

        elif score >= 20:
            level = "MEDIUM"

        else:
            level = "LOW"


        return level, score