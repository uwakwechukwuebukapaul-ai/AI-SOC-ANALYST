"""
Sentinel DNA
Autonomous Security Learning Engine

Responsible for:
- capturing security lessons
- analyzing operational patterns
- improving agent knowledge
- generating learning recommendations
- tracking learning evolution
"""

from datetime import datetime, timezone
from uuid import uuid4


class AutonomousSecurityLearningEngine:

    def __init__(self):
        self.lessons = []
        self.knowledge = {}
        self.history = []


    def _generate_id(self):
        return f"LEARN-{uuid4().hex[:8].upper()}"


    def record_security_lesson(
        self,
        incident_type,
        outcome,
        lesson
    ):
        record = {
            "lesson_id": self._generate_id(),
            "incident_type": incident_type,
            "outcome": outcome,
            "lesson": lesson,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.lessons.append(record)

        self.history.append({
            "action": "lesson_recorded",
            "data": record
        })

        return record


    def analyze_learning_pattern(self):

        patterns = {}

        for lesson in self.lessons:
            incident = lesson["incident_type"]

            patterns[incident] = (
                patterns.get(incident, 0) + 1
            )

        result = {
            "patterns": patterns,
            "total_lessons": len(self.lessons)
        }

        self.history.append({
            "action": "pattern_analysis",
            "data": result
        })

        return result


    def update_agent_knowledge(
        self,
        agent,
        knowledge_update
    ):

        if agent not in self.knowledge:
            self.knowledge[agent] = []

        self.knowledge[agent].append(
            knowledge_update
        )

        result = {
            "agent": agent,
            "knowledge_count": len(
                self.knowledge[agent]
            )
        }

        self.history.append({
            "action": "knowledge_update",
            "data": result
        })

        return result


    def generate_learning_recommendation(
        self,
        pattern_data
    ):

        recommendations = []

        if pattern_data.get(
            "total_lessons",
            0
        ) > 0:

            recommendations.append(
                "Improve detection rules using historical lessons"
            )

            recommendations.append(
                "Update autonomous response strategies"
            )

        result = {
            "recommendations": recommendations,
            "confidence": 0.9
        }

        self.history.append({
            "action": "recommendation_generated",
            "data": result
        })

        return result


    def calculate_learning_confidence(
        self,
        successful_cases,
        total_cases
    ):

        if total_cases == 0:
            return {
                "confidence": 0
            }

        confidence = (
            successful_cases /
            total_cases
        )

        result = {
            "confidence": round(
                confidence,
                2
            )
        }

        self.history.append({
            "action": "confidence_calculated",
            "data": result
        })

        return result


    def get_history(self):

        return self.history