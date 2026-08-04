"""
Sentinel DNA
Autonomous Security Agent Memory Engine

Provides persistent memory capabilities for autonomous security agents:
- Store experiences
- Retrieve historical intelligence
- Track successful actions
- Maintain agent learning context
"""

from datetime import datetime, timezone


class AutonomousSecurityAgentMemoryEngine:
    def __init__(self):
        self.memories = []
        self.agent_memory_index = {}

    def _timestamp(self):
        return datetime.now(timezone.utc).isoformat()

    def store_memory(
        self,
        agent_id,
        memory_type,
        event,
        context=None,
        outcome=None,
        confidence=0.0,
    ):
        memory = {
            "memory_id": f"MEM-{len(self.memories)+1:06d}",
            "agent_id": agent_id,
            "memory_type": memory_type,
            "event": event,
            "context": context or {},
            "outcome": outcome,
            "confidence": confidence,
            "created_at": self._timestamp(),
        }

        self.memories.append(memory)

        if agent_id not in self.agent_memory_index:
            self.agent_memory_index[agent_id] = []

        self.agent_memory_index[agent_id].append(memory["memory_id"])

        return memory

    def retrieve_memory(self, agent_id):
        results = []

        memory_ids = self.agent_memory_index.get(agent_id, [])

        for memory in self.memories:
            if memory["memory_id"] in memory_ids:
                results.append(memory)

        return results

    def search_memory(self, keyword):
        keyword = keyword.lower()

        results = []

        for memory in self.memories:
            searchable = (
                str(memory["event"])
                + str(memory["context"])
                + str(memory["outcome"])
            ).lower()

            if keyword in searchable:
                results.append(memory)

        return results

    def analyze_memory_pattern(self, agent_id):
        memories = self.retrieve_memory(agent_id)

        if not memories:
            return {
                "agent_id": agent_id,
                "memory_count": 0,
                "patterns": [],
                "status": "no_memory",
            }

        successful = [
            m for m in memories
            if str(m["outcome"]).lower() == "success"
        ]

        failed = [
            m for m in memories
            if str(m["outcome"]).lower() == "failure"
        ]

        return {
            "agent_id": agent_id,
            "memory_count": len(memories),
            "successful_actions": len(successful),
            "failed_actions": len(failed),
            "patterns": list(
                set(
                    m["memory_type"]
                    for m in memories
                )
            ),
            "status": "analyzed",
            "timestamp": self._timestamp(),
        }

    def generate_learning_recommendation(self, agent_id):
        analysis = self.analyze_memory_pattern(agent_id)

        if analysis["memory_count"] == 0:
            recommendation = "Collect more operational experience."

        elif analysis.get("failed_actions", 0) > 0:
            recommendation = (
                "Review failed operations and optimize decision strategy."
            )

        else:
            recommendation = (
                "Maintain current strategy and expand knowledge coverage."
            )

        return {
            "agent_id": agent_id,
            "recommendation": recommendation,
            "generated_at": self._timestamp(),
        }

    def memory_history(self):
        return self.memories