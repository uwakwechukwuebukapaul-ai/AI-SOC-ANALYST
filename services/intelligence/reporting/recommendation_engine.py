"""
Sentinel DNA Recommendation Engine
"""


class RecommendationEngine:


    def generate(
        self,
        severity: str,
    ) -> list[str]:


        if severity == "CRITICAL":

            return [
                "Isolate affected assets",
                "Block malicious indicators",
                "Start incident response workflow",
            ]


        if severity == "HIGH":

            return [
                "Investigate affected users",
                "Enrich indicators",
                "Monitor related activity",
            ]


        return [
            "Continue monitoring",
        ]