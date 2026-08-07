"""
Autonomous Security Agent Evaluation Engine

Evaluates Sentinel DNA autonomous agents.

Responsibilities:
- Register agent evaluation profiles
- Record mission outcomes
- Calculate performance metrics
- Evaluate confidence calibration
- Generate improvement recommendations
- Maintain evaluation history
"""

from datetime import datetime, timezone


class AutonomousSecurityAgentEvaluationEngine:

    def __init__(self):
        self.agents = {}
        self.evaluations = []
        self.history = []

    def register_agent(self, agent_id, name, role):

        agent = {
            "agent_id": agent_id,
            "name": name,
            "role": role,
            "missions": 0,
            "successful_missions": 0,
            "accuracy": 0,
            "confidence": 0,
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.agents[agent_id] = agent

        self.history.append({
            "event": "agent_registered",
            "agent_id": agent_id,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return agent

    def record_mission_result(
        self,
        agent_id,
        success,
        accuracy,
        confidence
    ):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        agent["missions"] += 1

        if success:
            agent["successful_missions"] += 1

        agent["accuracy"] = accuracy
        agent["confidence"] = confidence

        evaluation = {
            "agent_id": agent_id,
            "success": success,
            "accuracy": accuracy,
            "confidence": confidence,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.evaluations.append(evaluation)
        self.history.append(evaluation)

        return evaluation

    def calculate_performance_score(self, agent_id):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        if agent["missions"] == 0:
            success_rate = 0

        else:
            success_rate = (
                agent["successful_missions"]
                /
                agent["missions"]
            )

        performance_score = round(
            (
                success_rate * 0.5
                +
                agent["accuracy"] * 0.3
                +
                agent["confidence"] * 0.2
            ),
            2
        )

        return {
            "agent_id": agent_id,
            "success_rate": success_rate,
            "performance_score": performance_score
        }

    def evaluate_agent_quality(self, agent_id):

        result = self.calculate_performance_score(agent_id)

        score = result.get(
            "performance_score",
            0
        )

        if score >= 0.85:
            quality = "excellent"

        elif score >= 0.65:
            quality = "good"

        elif score >= 0.4:
            quality = "needs_improvement"

        else:
            quality = "critical"

        return {
            "agent_id": agent_id,
            "quality": quality,
            "score": score,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def generate_improvement_recommendation(self, agent_id):

        evaluation = self.evaluate_agent_quality(agent_id)

        quality = evaluation["quality"]

        if quality == "critical":
            recommendation = "retrain_agent"

        elif quality == "needs_improvement":
            recommendation = "increase_training"

        elif quality == "good":
            recommendation = "optimize_behavior"

        else:
            recommendation = "maintain_operation"

        result = {
            "agent_id": agent_id,
            "recommendation": recommendation,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.history.append(result)

        return result

    def evaluation_history(self):

        return self.history
