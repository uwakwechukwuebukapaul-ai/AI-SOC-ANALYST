"""
Runtime Intelligence Router Tests
"""

from services.intelligence.runtime.runtime_intelligence_router import (
    RuntimeIntelligenceRouter,
)



def test_init():

    router = RuntimeIntelligenceRouter()

    assert (
        router.routed
        ==
        0
    )



def test_register():

    router = RuntimeIntelligenceRouter()


    router.register(
        "ioc_lookup",
        lambda data: data,
    )


    assert (
        router.available(
            "ioc_lookup"
        )
        is True
    )



def test_route():

    router = RuntimeIntelligenceRouter()


    router.register(
        "analysis",
        lambda data: {
            "result":
                data["value"]
        },
    )


    result = router.route(
        "analysis",
        {
            "value": 5
        },
    )


    assert (
        result["result"]
        ==
        5
    )



def test_missing_route():

    router = RuntimeIntelligenceRouter()


    result = router.route(
        "unknown",
        {},
    )


    assert result is None



def test_clear():

    router = RuntimeIntelligenceRouter()


    router.register(
        "test",
        lambda data: data,
    )


    router.clear()


    assert (
        router.available(
            "test"
        )
        is False
    )



def test_status():

    router = RuntimeIntelligenceRouter()


    result = router.status()


    assert "capabilities" in result

    assert "routed" in result