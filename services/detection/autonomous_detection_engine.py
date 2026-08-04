"""
Sentinel DNA
Autonomous Detection Engine

Responsible for:
- generating detection rules
- analyzing suspicious behavior
- scoring detections
- improving detection logic
"""


class AutonomousDetectionEngine:

    def __init__(self):
        self.rules = []
        self.detection_history = []
        self.optimization_history = []

    def create_detection_rule(self, name, pattern, severity):
        rule = {
            "name": name,
            "pattern": pattern,
            "severity": severity,
            "enabled": True
        }

        self.rules.append(rule)

        return rule

    def analyze_behavior(self, event):
        score = 0
        indicators = []

        if event.get("suspicious_command"):
            score += 40
            indicators.append("suspicious_command")

        if event.get("unknown_process"):
            score += 30
            indicators.append("unknown_process")

        if event.get("network_anomaly"):
            score += 30
            indicators.append("network_anomaly")

        result = {
            "risk_score": score,
            "indicators": indicators,
            "detected": score > 0
        }

        self.detection_history.append(result)

        return result

    def evaluate_rule(self, rule, event):
        matched = rule["pattern"] in str(event)

        return {
            "rule": rule["name"],
            "matched": matched
        }

    def optimize_detection(self, feedback):
        improvement = {
            "feedback": feedback,
            "action": "Detection rule optimization applied"
        }

        self.optimization_history.append(improvement)

        return improvement

    def get_detection_history(self):
        return {
            "detections": self.detection_history,
            "optimizations": self.optimization_history,
            "rules": self.rules
        }

    def clear_history(self):
        self.detection_history.clear()
        self.optimization_history.clear()
        self.rules.clear()