"""
Autonomous Security Evaluation Engine

Evaluates security intelligence outputs,
agent decisions, investigations, and response quality.
"""

from datetime import datetime


class AutonomousSecurityEvaluationEngine:
    def __init__(self):
        self.evaluations = []

    def evaluate_security_event(self, event):
        risk_score = event.get("risk_score", 0)

        if risk_score >= 80:
            rating = "CRITICAL"
        elif risk_score >= 50:
            rating = "HIGH"
        elif risk_score >= 20:
            rating = "MEDIUM"
        else:
            rating = "LOW"

        result = {
            "event": event,
            "evaluation": rating,
            "accuracy_score": self._calculate_accuracy(event),
            "created_at": datetime.utcnow().isoformat()
        }

        self.evaluations.append(result)

        return result

    def _calculate_accuracy(self, event):
        confidence = event.get("confidence", 0)

        if confidence >= 90:
            return "EXCELLENT"
        elif confidence >= 70:
            return "GOOD"
        elif confidence >= 40:
            return "FAIR"

        return "POOR"

    def evaluate_agent_performance(self, agent):
        score = agent.get("success_rate", 0)

        if score >= 90:
            status = "OPTIMAL"
        elif score >= 70:
            status = "STABLE"
        else:
            status = "NEEDS_IMPROVEMENT"

        result = {
            "agent": agent,
            "performance": status,
            "created_at": datetime.utcnow().isoformat()
        }

        self.evaluations.append(result)

        return result

    def generate_quality_report(self):
        return {
            "total_evaluations": len(self.evaluations),
            "evaluations": self.evaluations
        }

    def get_history(self):
        return self.evaluations

    def clear_history(self):
        self.evaluations.clear()