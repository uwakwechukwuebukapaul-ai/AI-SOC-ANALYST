"""
Autonomous Security Evaluation Engine

Sentinel DNA Continuous Intelligence Evaluation Layer

Responsibilities:
- evaluate agent performance
- measure detection accuracy
- score decision quality
- evaluate investigation quality
- generate evaluation reports
- maintain evaluation history
"""

from datetime import datetime, timezone


class AutonomousSecurityEvaluationEngine:

    def __init__(self):
        self.history = []

    def evaluate_agent_performance(
        self,
        agent_name,
        success_rate
    ):

        result = {
            "agent": agent_name,
            "performance_score": success_rate,
            "status": (
                "excellent"
                if success_rate >= 90
                else "needs_improvement"
            )
        }

        self.history.append(result)

        return result

    def detection_accuracy_score(
        self,
        detected,
        total
    ):

        score = 0

        if total > 0:
            score = round(
                (detected / total) * 100,
                2
            )

        result = {
            "metric": "detection_accuracy",
            "score": score
        }

        self.history.append(result)

        return result

    def decision_quality_score(
        self,
        correct_decisions,
        total_decisions
    ):

        score = 0

        if total_decisions > 0:
            score = round(
                (correct_decisions / total_decisions)
                * 100,
                2
            )

        result = {
            "metric": "decision_quality",
            "score": score
        }

        self.history.append(result)

        return result

    def investigation_quality_score(
        self,
        evidence_quality,
        reasoning_quality
    ):

        score = round(
            (
                evidence_quality
                +
                reasoning_quality
            ) / 2,
            2
        )

        result = {
            "metric": "investigation_quality",
            "score": score
        }

        self.history.append(result)

        return result

    def generate_evaluation_report(
        self,
        system_name,
        metrics
    ):

        report = {
            "system": system_name,
            "metrics": metrics,
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.history.append(report)

        return report

    def get_history(self):

        return self.history