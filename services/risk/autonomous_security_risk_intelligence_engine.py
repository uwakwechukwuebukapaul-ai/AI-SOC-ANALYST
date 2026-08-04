"""
Autonomous Security Risk Intelligence Engine

Provides:
- Asset risk scoring
- Threat risk analysis
- Identity risk analysis
- Business impact evaluation
- Autonomous risk prioritization
"""

from datetime import datetime, timezone


class AutonomousSecurityRiskIntelligenceEngine:

    def __init__(self):
        self.risk_history = []
        self.assets = {}
        self.threats = {}

    def register_asset(self, asset_id, asset_type, criticality):
        asset = {
            "asset_id": asset_id,
            "asset_type": asset_type,
            "criticality": criticality,
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.assets[asset_id] = asset
        return asset

    def analyze_asset_risk(self, asset_id, vulnerabilities, exposure):
        asset = self.assets.get(asset_id)

        if not asset:
            return None

        score = (
            vulnerabilities * 10 +
            exposure * 5 +
            asset["criticality"] * 15
        )

        risk = {
            "asset_id": asset_id,
            "risk_score": score,
            "risk_level": self._risk_level(score),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.risk_history.append(risk)

        return risk

    def analyze_threat_risk(self, threat_name, severity, confidence):
        score = severity * confidence

        threat = {
            "threat": threat_name,
            "risk_score": score,
            "risk_level": self._risk_level(score),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.threats[threat_name] = threat
        self.risk_history.append(threat)

        return threat

    def analyze_identity_risk(self, user, failed_logins, privilege_level):
        score = (
            failed_logins * 10 +
            privilege_level * 20
        )

        result = {
            "user": user,
            "identity_risk_score": score,
            "risk_level": self._risk_level(score),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.risk_history.append(result)

        return result

    def calculate_business_impact(self, asset_value, downtime_hours):
        impact = (
            asset_value * 10 +
            downtime_hours * 5
        )

        return {
            "business_impact_score": impact,
            "impact_level": self._risk_level(impact)
        }

    def generate_risk_priority(self):
        if not self.risk_history:
            return []

        return sorted(
            self.risk_history,
            key=lambda item: item.get(
                "risk_score",
                item.get("identity_risk_score", 0)
            ),
            reverse=True
        )

    def generate_risk_report(self):
        return {
            "total_records": len(self.risk_history),
            "highest_risk": self.generate_risk_priority()[:5],
            "generated_at": datetime.now(timezone.utc).isoformat()
        }

    def risk_history_records(self):
        return self.risk_history

    def _risk_level(self, score):

        if score >= 80:
            return "CRITICAL"

        if score >= 50:
            return "HIGH"

        if score >= 25:
            return "MEDIUM"

        return "LOW"