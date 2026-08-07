class RuleValidator:


    def validate(
        self,
        rule
    ):


        required = [

            "title",
            "description",
            "level"

        ]


        valid = all(

            field in rule

            for field in required

        )


        return {

            "valid":
                valid,

            "missing":

                [

                    field

                    for field in required

                    if field not in rule

                ]

        }