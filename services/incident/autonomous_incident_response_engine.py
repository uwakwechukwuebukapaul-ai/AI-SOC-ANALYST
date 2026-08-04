"""
Sentinel DNA - Autonomous Incident Response Engine

Responsible for:
- Incident classification
- Severity assessment
- Response workflow generation
- Containment recommendations
- Incident lifecycle tracking
- Post incident learning signals
"""

from datetime import datetime


class AutonomousIncidentResponseEngine:

    def __init__(self):
        self.incidents = []
        self.response_history = []

    def create_incident(self, incident_data):
        incident = {
            "id": len(self.incidents) + 1,
            "title": incident_data.get("title"),
            "category": incident_data.get("category", "unknown"),
            "severity": self.calculate_severity(incident_data),
            "status": "open",
            "created_at": datetime.utcnow().isoformat()
        }

        self.incidents.append(incident)

        return incident

    def calculate_severity(self, incident_data):
        risk_score = incident_data.get("risk_score", 0)

        if risk_score >= 90:
            return "critical"

        if risk_score >= 70:
            return "high"

        if risk_score >= 40:
            return "medium"

        return "low"

    def generate_response_plan(self, incident):

        severity = incident.get("severity")

        plan = {
            "incident_id": incident.get("id"),
            "actions": []
        }

        if severity == "critical":
            plan["actions"] = [
                "isolate affected assets",
                "collect forensic evidence",
                "disable compromised accounts",
                "escalate to security leadership"
            ]

        elif severity == "high":
            plan["actions"] = [
                "investigate indicators",
                "contain affected systems",
                "collect evidence"
            ]

        else:
            plan["actions"] = [
                "monitor activity",
                "perform analyst review"
            ]

        self.response_history.append(plan)

        return plan

    def recommend_containment(self, incident):

        recommendations = []

        if incident.get("category") == "malware":
            recommendations.append("isolate endpoint")

        if incident.get("category") == "credential_compromise":
            recommendations.append("reset compromised credentials")

        if not recommendations:
            recommendations.append("perform manual investigation")

        return recommendations

    def update_status(self, incident_id, status):

        for incident in self.incidents:

            if incident["id"] == incident_id:
                incident["status"] = status
                return incident

        return None

    def get_incident_history(self):
        return self.incidents

    def get_response_history(self):
        return self.response_history

    def clear_history(self):

        self.incidents.clear()
        self.response_history.clear()