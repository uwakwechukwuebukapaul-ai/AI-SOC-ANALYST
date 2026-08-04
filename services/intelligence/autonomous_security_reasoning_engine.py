"""
Autonomous Security Reasoning Engine

Core reasoning layer for Sentinel DNA.

Responsibilities:
- Analyze security context
- Correlate evidence, threats, and incidents
- Generate reasoning decisions
- Recommend analyst actions
- Maintain reasoning history
"""

from datetime import datetime, timezone


class AutonomousSecurityReasoningEngine:
    def __init__(self):
        self.reasoning_history = []

    def analyze_security_context(self, context):
        risk_score = context.get("risk_score", 0)
        threats = context.get("threats", [])
        evidence = context.get("evidence", [])

        if risk_score >= 80:
            severity = "CRITICAL"
            decision = "Immediate containment recommended"
        elif risk_score >= 50:
            severity = "HIGH"
            decision = "Investigation and monitoring required"
        else:
            severity = "LOW"
            decision = "Continue observation"

        reasoning = {
            "severity": severity,
            "decision": decision,
            "threat_count": len(threats),
            "evidence_count": len(evidence),
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.reasoning_history.append(reasoning)

        return reasoning

    def generate_recommendation(self, analysis):
        severity = analysis.get("severity")

        recommendations = {
            "CRITICAL": [
                "Contain affected assets",
                "Collect forensic evidence",
                "Escalate incident"
            ],
            "HIGH": [
                "Perform deeper investigation",
                "Validate indicators",
                "Monitor activity"
            ],
            "LOW": [
                "Continue monitoring",
                "Collect additional telemetry"
            ]
        }

        return recommendations.get(
            severity,
            ["Review security context"]
        )

    def correlate_threat_intelligence(self, indicators):
        matches = []

        for indicator in indicators:
            if indicator.get("malicious"):
                matches.append({
                    "indicator": indicator.get("value"),
                    "confidence": "HIGH"
                })

        return matches

    def explain_decision(self, reasoning):
        return {
            "summary": reasoning.get("decision"),
            "reason": (
                f"Decision generated from "
                f"{reasoning.get('threat_count')} threats "
                f"and {reasoning.get('evidence_count')} evidence items."
            )
        }

    def get_reasoning_history(self):
        return self.reasoning_history

    def clear_history(self):
        self.reasoning_history.clear()