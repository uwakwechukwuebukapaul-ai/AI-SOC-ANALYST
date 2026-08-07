class QueryBuilder:


    def build(
        self,
        indicator
    ):

        return {

            "query":
                f"SEARCH indicator={indicator}",

            "type":
                "threat_hunting_query"

        }