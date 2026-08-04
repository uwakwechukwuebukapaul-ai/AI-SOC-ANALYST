"""
Agent Learning Engine

Responsible for:
- learning from agent execution history
- calculating performance scores
- generating optimization recommendations
- improving future agent selection
"""


class AgentLearningEngine:

    def __init__(self):
        self.learning_records = []

    def record_feedback(
        self,
        agent_name,
        task,
        success,
        confidence,
        execution_time=0
    ):
        """
        Store agent performance feedback.
        """

        record = {
            "agent": agent_name,
            "task": task,
            "success": success,
            "confidence": confidence,
            "execution_time": execution_time,
        }

        self.learning_records.append(record)

        return record


    def get_agent_performance(self, agent_name):
        """
        Calculate agent performance metrics.
        """

        records = [
            r for r in self.learning_records
            if r["agent"] == agent_name
        ]

        if not records:
            return {
                "agent": agent_name,
                "success_rate": 0,
                "average_confidence": 0,
                "executions": 0,
            }

        success_rate = (
            sum(1 for r in records if r["success"])
            / len(records)
        ) * 100

        confidence = (
            sum(r["confidence"] for r in records)
            / len(records)
        )

        return {
            "agent": agent_name,
            "success_rate": success_rate,
            "average_confidence": confidence,
            "executions": len(records),
        }


    def recommend_agent(self, agents):
        """
        Recommend highest performing agent.

        agents:
        [
            "agent_name",
            ...
        ]
        """

        ranking = []

        for agent in agents:
            performance = self.get_agent_performance(agent)

            score = (
                performance["success_rate"]
                +
                performance["average_confidence"]
            )

            ranking.append(
                {
                    "agent": agent,
                    "score": score,
                }
            )

        if not ranking:
            return None

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranking[0]


    def learning_history(self):
        """
        Return all learning events.
        """

        return self.learning_records


    def clear_learning(self):
        """
        Reset learning data.
        """

        self.learning_records.clear()

        return True