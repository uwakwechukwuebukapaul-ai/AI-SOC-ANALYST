"""
Sentinel DNA
Autonomous Threat Intelligence Engine

Responsible for:
- IOC intelligence management
- threat actor profiling
- threat scoring
- MITRE ATT&CK mapping
- campaign intelligence tracking
- intelligence history
"""

from datetime import datetime, timezone
from uuid import uuid4


class AutonomousThreatIntelligenceEngine:

    def __init__(self):
        self.indicators = []
        self.threat_actors = {}
        self.campaigns = {}
        self.history = []


    def _generate_id(self):
        return f"TI-{uuid4().hex[:8].upper()}"


    def register_indicator(
        self,
        indicator_type,
        value,
        confidence
    ):

        indicator = {
            "id": self._generate_id(),
            "type": indicator_type,
            "value": value,
            "confidence": confidence,
            "status": "active",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.indicators.append(indicator)

        self.history.append({
            "action": "indicator_registered",
            "data": indicator
        })

        return indicator



    def analyze_indicator(self, indicator):

        confidence = indicator.get(
            "confidence",
            0
        )

        if confidence >= 0.8:
            severity = "high"

        elif confidence >= 0.5:
            severity = "medium"

        else:
            severity = "low"


        result = {
            "indicator": indicator["value"],
            "risk": severity,
            "confidence": confidence
        }

        self.history.append({
            "action": "indicator_analysis",
            "data": result
        })

        return result



    def create_threat_actor_profile(
        self,
        actor_name,
        techniques
    ):

        profile = {
            "actor": actor_name,
            "techniques": techniques,
            "created": datetime.now(
                timezone.utc
            ).isoformat()
        }


        self.threat_actors[
            actor_name
        ] = profile


        self.history.append({
            "action": "actor_profile_created",
            "data": profile
        })


        return profile



    def map_attack_techniques(
        self,
        techniques
    ):

        mapping = {
            "credential_access":
                "T1003",
            "phishing":
                "T1566",
            "malware_execution":
                "T1204"
        }


        result = []

        for technique in techniques:

            if technique in mapping:

                result.append({
                    "technique": technique,
                    "attack_id": mapping[technique]
                })


        self.history.append({
            "action": "attack_mapping",
            "data": result
        })


        return result



    def track_campaign(
        self,
        campaign_name,
        indicators
    ):

        campaign = {
            "name": campaign_name,
            "indicators": indicators,
            "status": "monitoring",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }


        self.campaigns[
            campaign_name
        ] = campaign


        self.history.append({
            "action": "campaign_tracking",
            "data": campaign
        })


        return campaign



    def calculate_threat_score(
        self,
        confidence,
        impact
    ):

        score = (
            confidence +
            impact
        ) / 2


        result = {
            "threat_score": round(
                score,
                2
            ),
            "classification":
                "critical"
                if score >= 0.8
                else "moderate"
        }


        self.history.append({
            "action": "threat_scoring",
            "data": result
        })


        return result



    def get_history(self):

        return self.history