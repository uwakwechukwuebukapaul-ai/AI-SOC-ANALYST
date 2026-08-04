"""
Sentinel DNA
Autonomous Security Agent Learning Engine

Provides continuous improvement capabilities for autonomous security agents:
- Learn from historical missions
- Analyze behavior patterns
- Extract operational knowledge
- Recommend improvements
- Track learning evolution
"""

from datetime import datetime, timezone


class AutonomousSecurityAgentLearningEngine:

    def __init__(self):
        self.learning_records = []
        self.agent_profiles = {}

    def _timestamp(self):
        return datetime.now(timezone.utc).isoformat()

    def register_agent(self, agent_id, capabilities=None):
        profile = {
            "agent_id": agent_id,
            "capabilities": capabilities or [],
            "learning_score": 0,
            "registered_at": self._timestamp(),
        }

        self.agent_profiles[agent_id] = profile

        return profile

    def record_learning_event(
        self,
        agent_id,
        event_type,
        observation,
        result,
        improvement_area=None,
    ):
        record = {
            "learning_id": f"LEARN-{len(self.learning_records)+1:06d}",
            "agent_id": agent_id,
            "event_type": event_type,
            "observation": observation,
            "result": result,
            "improvement_area": improvement_area,
            "timestamp": self._timestamp(),
        }

        self.learning_records.append(record)

        if agent_id in self.agent_profiles:
            self.agent_profiles[agent_id]["learning_score"] += 1

        return record

    def analyze_learning_pattern(self, agent_id):

        records = [
            record
            for record in self.learning_records
            if record["agent_id"] == agent_id
        ]

        if not records:
            return {
                "agent_id": agent_id,
                "learning_events": 0,
                "status": "no_learning_data",
            }

        improvement_areas = list(
            set(
                record["improvement_area"]
                for record in records
                if record["improvement_area"]
            )
        )

        successes = [
            record
            for record in records
            if str(record["result"]).lower() == "success"
        ]

        failures = [
            record
            for record in records
            if str(record["result"]).lower() == "failure"
        ]

        return {
            "agent_id": agent_id,
            "learning_events": len(records),
            "successful_learning": len(successes),
            "failed_learning": len(failures),
            "improvement_areas": improvement_areas,
            "status": "analyzed",
            "timestamp": self._timestamp(),
        }

    def generate_learning_strategy(self, agent_id):

        analysis = self.analyze_learning_pattern(agent_id)

        if analysis["learning_events"] == 0:
            strategy = (
                "Collect more operational experiences before optimization."
            )

        elif analysis.get("failed_learning", 0) > 0:
            strategy = (
                "Prioritize failed scenarios and improve decision accuracy."
            )

        else:
            strategy = (
                "Expand successful behavior patterns into future missions."
            )

        return {
            "agent_id": agent_id,
            "strategy": strategy,
            "generated_at": self._timestamp(),
        }

    def evaluate_agent_growth(self, agent_id):

        profile = self.agent_profiles.get(agent_id)

        if not profile:
            return {
                "agent_id": agent_id,
                "status": "unknown_agent",
            }

        score = profile["learning_score"]

        if score >= 5:
            level = "advanced"

        elif score >= 2:
            level = "developing"

        else:
            level = "initial"

        return {
            "agent_id": agent_id,
            "learning_score": score,
            "growth_level": level,
            "timestamp": self._timestamp(),
        }

    def learning_history(self):
        return self.learning_records