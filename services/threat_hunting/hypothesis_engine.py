class HypothesisEngine:


    def create(
        self,
        behavior
    ):

        return {

            "type":
                "hunt_hypothesis",

            "behavior":
                behavior,

            "indicator":
                behavior.get(
                    "indicator"
                )

        }