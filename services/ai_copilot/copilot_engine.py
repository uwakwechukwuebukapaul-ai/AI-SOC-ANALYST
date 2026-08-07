from datetime import datetime, timezone


class AICopilotEngine:


    def __init__(self):

        self.sessions = []


    def analyze_case(
        self,
        case,
        decision
    ):

        analysis = {

            "type": "copilot_analysis",

            "case": case,

            "summary":
                self._generate_summary(
                    case,
                    decision
                ),

            "reasoning":
                self._generate_reasoning(
                    decision
                ),

            "recommendations":
                self._recommend_actions(
                    decision
                ),

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.sessions.append(
            analysis
        )


        return analysis



    def _generate_summary(
        self,
        case,
        decision
    ):

        threat = decision.get(
            "threat_level",
            "unknown"
        )


        return (
            f"Security investigation detected "
            f"{threat} level activity "
            f"for case {case.get('id','unknown')}."
        )



    def _generate_reasoning(
        self,
        decision
    ):

        return [

            "Risk intelligence evaluated",

            "Threat correlations reviewed",

            f"Confidence score: "
            f"{decision.get('confidence',0)}"

        ]



    def _recommend_actions(
        self,
        decision
    ):

        recommendation = decision.get(
            "recommendation"
        )


        return [
            recommendation
        ]