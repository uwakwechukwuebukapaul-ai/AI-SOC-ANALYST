from datetime import datetime, timezone


class AutonomousSecurityMetaIntelligenceEngine:
    """
    Autonomous Security Meta Intelligence Engine

    Responsible for:
    - managing intelligence modules
    - analyzing SOC ecosystem state
    - selecting optimal intelligence engines
    - generating autonomous strategies
    - confidence estimation
    """

    def __init__(self):
        self.modules = {}
        self.history = []


    def register_intelligence_module(self, name, capabilities):
        module = {
            "name": name,
            "capabilities": capabilities,
            "status": "active",
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.modules[name] = module

        self.history.append({
            "action": "register_module",
            "module": name,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return module


    def analyze_system_state(self):

        active_modules = [
            name for name, module in self.modules.items()
            if module["status"] == "active"
        ]

        state = {
            "total_modules": len(self.modules),
            "active_modules": active_modules,
            "health": "optimal" if active_modules else "degraded",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.history.append({
            "action": "system_analysis",
            "result": state
        })

        return state


    def select_optimal_engine(self, requirement):

        for name, module in self.modules.items():

            if requirement in module["capabilities"]:

                result = {
                    "selected_engine": name,
                    "reason": "capability_match",
                    "confidence": 0.95
                }

                self.history.append({
                    "action": "engine_selection",
                    "result": result
                })

                return result


        result = {
            "selected_engine": None,
            "reason": "no_matching_engine",
            "confidence": 0.20
        }

        self.history.append({
            "action": "engine_selection",
            "result": result
        })

        return result


    def generate_autonomous_strategy(self, threat_state):

        severity = threat_state.get(
            "severity",
            "medium"
        )


        if severity == "critical":

            strategy = {
                "priority": "immediate",
                "actions": [
                    "activate_response_engine",
                    "isolate_assets",
                    "start_investigation"
                ]
            }


        elif severity == "high":

            strategy = {
                "priority": "urgent",
                "actions": [
                    "increase_monitoring",
                    "collect_evidence"
                ]
            }


        else:

            strategy = {
                "priority": "normal",
                "actions": [
                    "continue_monitoring"
                ]
            }


        result = {
            "strategy": strategy,
            "confidence": 0.90,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }


        self.history.append({
            "action": "strategy_generation",
            "result": result
        })

        return result



    def calculate_meta_decision_confidence(
        self,
        intelligence_score,
        evidence_score
    ):

        confidence = (
            intelligence_score +
            evidence_score
        ) / 2


        result = {
            "confidence": round(confidence,2),
            "classification":
                "high"
                if confidence >= 0.8
                else "medium"
        }


        self.history.append({
            "action": "confidence_calculation",
            "result": result
        })

        return result



    def get_history(self):

        return self.history