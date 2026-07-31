"""
Sentinel DNA

Threat Scoring Engine

Calculates security risk
from collected evidence.
"""


class ThreatScorer:


    def __init__(self):

        self.weights = {


            "HIGH":

                10,


            "MEDIUM":

                5,


            "LOW":

                1

        }



    def score_email(
        self,
        email_result
    ):

        score = 0


        risk = email_result.get(
            "risk",
            "LOW"
        )


        score += self.weights.get(
            risk,
            0
        )


        score += len(

            email_result.get(
                "evidence",
                []

            )

        )


        return score




    def score_iocs(
        self,
        ioc_result
    ):


        score = 0


        indicators = ioc_result.get(
            "indicators",
            {}

        )


        if indicators.get("url"):

            score += 5



        if indicators.get("ipv4"):

            score += 3



        if indicators.get("md5"):

            score += 4



        if indicators.get("sha256"):

            score += 4



        if indicators.get("email"):

            score += 2



        return score





    def calculate_level(
        self,
        score
    ):


        if score >= 15:

            return "CRITICAL"



        elif score >= 8:

            return "HIGH"



        elif score >= 4:

            return "MEDIUM"



        else:

            return "LOW"





    def analyze(
        self,
        email_result=None,
        ioc_result=None
    ):


        total = 0



        if email_result:

            total += self.score_email(
                email_result
            )



        if ioc_result:

            total += self.score_iocs(
                ioc_result
            )



        return {


            "risk_score":

                total,


            "severity":

                self.calculate_level(
                    total
                ),


            "recommendation":

                self.recommend(
                    total
                )

        }





    def recommend(
        self,
        score
    ):


        if score >= 15:

            return (

                "Immediate containment required. "
                "Escalate to SOC response team."

            )


        elif score >= 8:

            return (

                "Investigate indicators and "
                "monitor affected systems."

            )


        else:

            return (

                "Continue monitoring."

            )



threat_scorer = ThreatScorer()