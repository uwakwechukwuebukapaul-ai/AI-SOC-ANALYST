class HuntResultManager:


    def summarize(
        self,
        result
    ):

        return {

            "matches_found":
                len(
                    result.get(
                        "matches",
                        []
                    )
                ),

            "status":
                result.get(
                    "status"
                )

        }