from datetime import datetime, timezone


class ReportGenerator:


    def generate(
        self,
        analysis
    ):


        return {

            "title":
                "Sentinel DNA Investigation Report",

            "summary":
                analysis.get(
                    "summary"
                ),

            "reasoning":
                analysis.get(
                    "reasoning"
                ),

            "actions":
                analysis.get(
                    "recommendations"
                ),

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }