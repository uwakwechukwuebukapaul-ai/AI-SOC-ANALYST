"""
Autonomous Security Digital Twin Engine

Simulates enterprise security posture, attack scenarios,
defense readiness, and autonomous improvement recommendations.

Part of Sentinel DNA autonomous intelligence layer.
"""

from datetime import datetime


class AutonomousSecurityDigitalTwinEngine:
    def __init__(self):
        self.assets = {}
        self.attack_scenarios = {}
        self.simulations = []
        self.history = []

    def register_asset(self, asset_id, asset_type, criticality):
        asset = {
            "asset_id": asset_id,
            "asset_type": asset_type,
            "criticality": criticality,
            "created_at": datetime.utcnow().isoformat()
        }

        self.assets[asset_id] = asset

        self.history.append({
            "action": "asset_registered",
            "asset": asset
        })

        return asset

    def create_attack_scenario(
        self,
        scenario_id,
        technique,
        severity
    ):
        scenario = {
            "scenario_id": scenario_id,
            "technique": technique,
            "severity": severity,
            "created_at": datetime.utcnow().isoformat()
        }

        self.attack_scenarios[scenario_id] = scenario

        self.history.append({
            "action": "attack_scenario_created",
            "scenario": scenario
        })

        return scenario

    def simulate_attack(
        self,
        asset_id,
        scenario_id
    ):
        asset = self.assets.get(asset_id)
        scenario = self.attack_scenarios.get(scenario_id)

        simulation = {
            "asset": asset,
            "scenario": scenario,
            "risk_score": self._calculate_risk(
                asset,
                scenario
            ),
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        }

        self.simulations.append(simulation)

        self.history.append({
            "action": "attack_simulation",
            "result": simulation
        })

        return simulation

    def analyze_security_posture(self):
        posture = {
            "assets": len(self.assets),
            "attack_scenarios": len(self.attack_scenarios),
            "simulations": len(self.simulations),
            "readiness_score": self._calculate_readiness()
        }

        self.history.append({
            "action": "posture_analysis",
            "result": posture
        })

        return posture

    def generate_improvement_strategy(self):
        strategy = {
            "recommendations": [
                "Improve detection coverage",
                "Optimize incident response automation",
                "Increase threat intelligence correlation",
                "Strengthen critical asset protection"
            ],
            "confidence": 0.92,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append({
            "action": "improvement_strategy",
            "result": strategy
        })

        return strategy

    def _calculate_risk(self, asset, scenario):
        if not asset or not scenario:
            return 0

        criticality_score = {
            "low": 20,
            "medium": 50,
            "high": 80,
            "critical": 95
        }.get(asset["criticality"], 50)

        severity_score = {
            "low": 20,
            "medium": 50,
            "high": 80,
            "critical": 95
        }.get(scenario["severity"], 50)

        return round(
            (criticality_score + severity_score) / 2,
            2
        )

    def _calculate_readiness(self):
        if not self.assets:
            return 0

        return min(
            100,
            len(self.simulations) * 20 + 50
        )

    def get_history(self):
        return self.history