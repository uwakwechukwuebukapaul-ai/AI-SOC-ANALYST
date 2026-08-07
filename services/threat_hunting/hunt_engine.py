from datetime import datetime, timezone


class HuntEngine:


    def __init__(self):

        self.hunts = []


    def execute_hunt(
        self,
        hypothesis,
        data
    ):

        result = {

            "type":
                "threat_hunt",

            "hypothesis":
                hypothesis,

            "matches":
                [],

            "status":
                "completed",

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        if hypothesis.get(
            "indicator"
        ):

            for item in data:

                if (
                    hypothesis["indicator"]
                    in str(item)
                ):

                    result["matches"].append(
                        item
                    )


        self.hunts.append(
            result
        )


        return result



    def history(self):

        return self.hunts