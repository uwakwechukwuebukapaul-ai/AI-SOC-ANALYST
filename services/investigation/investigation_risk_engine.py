"""
Sentinel DNA - Investigation Risk Intelligence Engine

Calculates dynamic investigation risk based on:
- Evidence severity
- IOC reputation
- Threat intelligence confidence
- MITRE ATT&CK techniques
- Correlation score
- Agent investigation findings

This layer converts investigation signals into
actionable risk classification.
"""


class InvestigationRiskEngine:

    def __init__(self):
        self.risk_history = []

    def calculate_risk(
        self,
        investigation_id,
        evidence_score=0,
        ioc_score=0,
        threat_score=0,
        technique_score=0,
        correlation_score=0,
        agent_score=0
    ):
        total_score = (
            evidence_score +
            ioc_score +
            threat_score +
            technique_score +
            correlation_score +
            agent_score
        )

        risk_level = self.classify_risk(total_score)

        result = {
            "investigation_id": investigation_id,
            "risk_score": total_score,
            "risk_level": risk_level,
            "components": {
                "evidence": evidence_score,
                "ioc": ioc_score,
                "threat": threat_score,
                "technique": technique_score,
                "correlation": correlation_score,
                "agent": agent_score
            }
        }

        self.risk_history.append(result)

        return result

    def classify_risk(self, score):

        if score >= 80:
            return "CRITICAL"

        if score >= 60:
            return "HIGH"

        if score >= 30:
            return "MEDIUM"

        return "LOW"

    def evaluate_correlation_risk(self, correlation_score):

        if correlation_score >= 80:
            return "CRITICAL"

        if correlation_score >= 50:
            return "HIGH"

        if correlation_score >= 20:
            return "MEDIUM"

        return "LOW"

    def get_risk_history(self):
        return self.risk_history

    def clear_history(self):
        self.risk_history = []