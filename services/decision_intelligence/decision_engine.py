from datetime import datetime, timezone


class DecisionIntelligenceEngine:

    def __init__(self):
        self.decisions = []


    def evaluate(
        self,
        investigation,
        risk,
        threat
    ):

        decision = {

            "type": "security_decision",

            "investigation": investigation,

            "risk_score": risk.get(
                "risk_score",
                0
            ),

            "threat_level": threat.get(
                "threat_level",
                "unknown"
            ),

            "confidence": self._calculate_confidence(
                risk,
                threat
            ),

            "recommendation":
                self._generate_recommendation(
                    risk,
                    threat
                ),

            "status": "completed",

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.decisions.append(
            decision
        )

        return decision



    def _calculate_confidence(
        self,
        risk,
        threat
    ):

        score = 0


        if risk.get(
            "risk_score",
            0
        ) > 70:

            score += 50


        if threat.get(
            "matches"
        ):

            score += 50


        return score



    def _generate_recommendation(
        self,
        risk,
        threat
    ):


        if risk.get(
            "risk_score",
            0
        ) >= 80:

            return (
                "Immediately isolate affected asset "
                "and begin incident response workflow"
            )


        if threat.get(
            "matches"
        ):

            return (
                "Investigate correlated indicators "
                "and collect additional evidence"
            )


        return (
            "Continue monitoring activity"
        )



    def history(self):

        return self.decisions