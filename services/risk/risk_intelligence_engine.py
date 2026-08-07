from datetime import datetime, timezone


class RiskIntelligenceEngine:

    def __init__(self):
        self.assessments = []


    def assess(self, intelligence):

        score = self.calculate_score(
            intelligence
        )

        assessment = {
            "type": "risk_assessment",
            "score": score,
            "severity": self.get_severity(score),
            "recommendation": self.get_action(score),
            "status": "completed",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.assessments.append(
            assessment
        )

        return assessment


    def calculate_score(self, intelligence):

        score = 0

        if intelligence.get("risk_score"):
            score += intelligence["risk_score"]

        if intelligence.get("severity") == "high":
            score += 30

        if intelligence.get("critical"):
            score += 40

        return min(score, 100)


    def get_severity(self, score):

        if score >= 80:
            return "critical"

        if score >= 50:
            return "high"

        if score >= 25:
            return "medium"

        return "low"


    def get_action(self, score):

        if score >= 80:
            return "immediate_containment"

        if score >= 50:
            return "investigate_and_monitor"

        return "continue_observation"