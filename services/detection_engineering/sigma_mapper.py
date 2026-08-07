class SigmaMapper:


    def map_detection(
        self,
        detection
    ):


        return {

            "format":
                "sigma",

            "rule":

                {
                    "title":
                    "Sentinel DNA Detection Rule",

                    "description":
                    "Generated detection logic",

                    "level":
                    detection.get(
                        "severity",
                        "medium"
                    )
                }

        }