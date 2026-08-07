"""
Autonomous Security Intelligence Core

Central reasoning layer for Sentinel DNA.

Responsibilities:
- Register intelligence components
- Analyze security situations
- Generate autonomous decisions
- Coordinate security agents
- Track intelligence cycles
- Maintain decision history
"""


from datetime import datetime, timezone


class AutonomousSecurityIntelligenceCore:

    def __init__(self):
        self.components = {}
        self.decisions = []
        self.cycles = []

    def register_component(self, component_id, name, category="security"):
        component = {
            "component_id": component_id,
            "name": name,
            "category": category,
            "status": "active",
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.components[component_id] = component

        return component

    def list_components(self):
        return list(self.components.values())

    def analyze_security_event(self, event):
        severity = event.get("severity", "low")

        risk_mapping = {
            "low": 20,
            "medium": 50,
            "high": 75,
            "critical": 95
        }

        risk_score = risk_mapping.get(severity, 20)

        analysis = {
            "event": event,
            "risk_score": risk_score,
            "risk_level": self._risk_level(risk_score),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        return analysis

    def generate_decision(self, analysis):
        risk_level = analysis["risk_level"]

        actions = {
            "LOW": "monitor_activity",
            "MEDIUM": "increase_monitoring",
            "HIGH": "start_investigation",
            "CRITICAL": "contain_threat"
        }

        decision = {
            "risk_level": risk_level,
            "recommended_action": actions.get(
                risk_level,
                "monitor_activity"
            ),
            "confidence": self._confidence(
                analysis["risk_score"]
            ),
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.decisions.append(decision)

        return decision

    def assign_agent(self, decision):

        action = decision["recommended_action"]

        agent_mapping = {
            "monitor_activity": "security_monitor_agent",
            "increase_monitoring": "threat_hunting_agent",
            "start_investigation": "investigation_agent",
            "contain_threat": "response_agent"
        }

        assignment = {
            "agent": agent_mapping.get(
                action,
                "security_agent"
            ),
            "action": action,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        return assignment

    def execute_intelligence_cycle(self, event):

        analysis = self.analyze_security_event(event)

        decision = self.generate_decision(
            analysis
        )

        assignment = self.assign_agent(
            decision
        )

        cycle = {
            "event": event,
            "analysis": analysis,
            "decision": decision,
            "assignment": assignment,
            "status": "completed",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.cycles.append(cycle)

        return cycle

    def record_learning_feedback(self, cycle_id, feedback):

        record = {
            "cycle_id": cycle_id,
            "feedback": feedback,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        return record

    def intelligence_history(self):

        return self.cycles

    def decision_history(self):

        return self.decisions

    def _risk_level(self, score):

        if score >= 90:
            return "CRITICAL"

        if score >= 70:
            return "HIGH"

        if score >= 40:
            return "MEDIUM"

        return "LOW"

    def _confidence(self, score):

        if score >= 90:
            return 0.95

        if score >= 70:
            return 0.85

        if score >= 40:
            return 0.70

        return 0.50
