from datetime import datetime, timezone


class AutonomousSOCCopilot:
    """
    Autonomous SOC Copilot Intelligence Engine

    Provides AI-style investigation reasoning,
    recommendations, explanations, and analyst assistance.
    """

    def __init__(self):
        self.investigations = []
        self.history = []

    def analyze_incident(self, incident_id, evidence):
        risk = self._calculate_risk(evidence)

        analysis = {
            "incident_id": incident_id,
            "risk_level": risk["level"],
            "risk_score": risk["score"],
            "findings": self._generate_findings(evidence),
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.investigations.append(analysis)

        self.history.append({
            "action": "incident_analyzed",
            "incident_id": incident_id,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return analysis

    def generate_recommendation(self, analysis):
        risk_level = analysis.get("risk_level")

        if risk_level == "CRITICAL":
            action = "Isolate endpoint and begin incident response workflow"

        elif risk_level == "HIGH":
            action = "Investigate user activity and collect additional evidence"

        elif risk_level == "MEDIUM":
            action = "Monitor activity and perform deeper analysis"

        else:
            action = "No immediate action required"

        recommendation = {
            "incident_id": analysis["incident_id"],
            "recommendation": action,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.history.append({
            "action": "recommendation_generated",
            "incident_id": analysis["incident_id"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return recommendation

    def explain_incident(self, analysis):
        explanation = {
            "incident_id": analysis["incident_id"],
            "explanation": (
                f"Incident classified as {analysis['risk_level']} "
                f"because security indicators matched "
                f"investigation criteria."
            ),
            "findings": analysis["findings"]
        }

        return explanation

    def find_similar_patterns(self, keyword):
        matches = []

        for investigation in self.investigations:
            if keyword.lower() in str(
                investigation
            ).lower():
                matches.append(investigation)

        return matches

    def _calculate_risk(self, evidence):
        score = 0

        if evidence.get("malware"):
            score += 40

        if evidence.get("credential_compromise"):
            score += 30

        if evidence.get("suspicious_network"):
            score += 20

        if score >= 70:
            level = "CRITICAL"

        elif score >= 40:
            level = "HIGH"

        elif score >= 20:
            level = "MEDIUM"

        else:
            level = "LOW"

        return {
            "score": score,
            "level": level
        }

    def _generate_findings(self, evidence):
        findings = []

        for key, value in evidence.items():
            if value:
                findings.append(key)

        return findings

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()
        self.investigations.clear()

        return True