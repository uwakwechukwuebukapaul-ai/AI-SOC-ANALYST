class AnalystAssistant:


    def explain(
        self,
        report
    ):

        return {

            "question":
                "Why is this incident important?",

            "answer":
                report.get(
                    "summary"
                )

        }