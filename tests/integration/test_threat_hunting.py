from services.threat_hunting import (
    HuntEngine,
    QueryBuilder,
    HypothesisEngine,
    HuntResultManager
)



def test_hypothesis_creation():

    engine = HypothesisEngine()


    result = engine.create(

        {
            "behavior":
                "credential_access",

            "indicator":
                "192.168.1.10"
        }

    )


    assert (
        result["type"]
        ==
        "hunt_hypothesis"
    )



def test_query_builder():

    builder = QueryBuilder()


    result = builder.build(
        "192.168.1.10"
    )


    assert (
        "SEARCH"
        in result["query"]
    )



def test_threat_hunt_execution():

    engine = HuntEngine()


    result = engine.execute_hunt(

        {
            "indicator":
                "192.168.1.10"
        },

        [
            {
                "ip":
                    "192.168.1.10"
            }
        ]

    )


    assert (
        len(
            result["matches"]
        )
        ==
        1
    )



def test_hunt_summary():

    manager = HuntResultManager()


    result = manager.summarize(

        {
            "matches":
                [
                    "event"
                ],

            "status":
                "completed"
        }

    )


    assert (
        result["matches_found"]
        ==
        1
    )