"""
Sentinel DNA
Autonomous Learning Engine

Responsible for:
- collecting investigation feedback
- evaluating outcomes
- storing learning patterns
- improving future autonomous decisions
"""


class AutonomousLearningEngine:
    def __init__(self):
        self.feedback_history = []
        self.learning_patterns = []
        self.agent_metrics = {}

    def store_feedback(self, investigation_id, outcome, feedback):
        record = {
            "investigation_id": investigation_id,
            "outcome": outcome,
            "feedback": feedback
        }

        self.feedback_history.append(record)

        self._generate_learning_pattern(record)

        return record

    def _generate_learning_pattern(self, feedback):
        pattern = {
            "trigger": feedback["outcome"],
            "lesson": feedback["feedback"]
        }

        self.learning_patterns.append(pattern)

    def analyze_agent_performance(self, agent_name, success, confidence):
        if agent_name not in self.agent_metrics:
            self.agent_metrics[agent_name] = {
                "executions": 0,
                "successes": 0,
                "confidence_total": 0
            }

        metrics = self.agent_metrics[agent_name]

        metrics["executions"] += 1

        if success:
            metrics["successes"] += 1

        metrics["confidence_total"] += confidence

        return self.get_agent_performance(agent_name)

    def get_agent_performance(self, agent_name):
        if agent_name not in self.agent_metrics:
            return None

        metrics = self.agent_metrics[agent_name]

        success_rate = (
            metrics["successes"] /
            metrics["executions"]
        )

        average_confidence = (
            metrics["confidence_total"] /
            metrics["executions"]
        )

        return {
            "agent": agent_name,
            "success_rate": success_rate,
            "average_confidence": average_confidence
        }

    def recommend_improvement(self, context):
        recommendations = []

        if context.get("false_positive"):
            recommendations.append(
                "Improve detection precision"
            )

        if context.get("slow_response"):
            recommendations.append(
                "Optimize response workflow"
            )

        if not recommendations:
            recommendations.append(
                "Maintain current strategy"
            )

        return recommendations

    def get_learning_history(self):
        return {
            "feedback": self.feedback_history,
            "patterns": self.learning_patterns,
            "agents": self.agent_metrics
        }

    def clear_history(self):
        self.feedback_history.clear()
        self.learning_patterns.clear()
        self.agent_metrics.clear()