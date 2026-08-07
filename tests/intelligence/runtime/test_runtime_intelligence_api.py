"""
Runtime Intelligence API Tests
"""

from services.intelligence.runtime.runtime_intelligence_api import (
    RuntimeIntelligenceAPI,
)



def test_init():

    api = RuntimeIntelligenceAPI()

    assert api.service is not None



def test_register():

    api = RuntimeIntelligenceAPI()


    api.register(
        "analysis",
        lambda ctx: {
            "status":
                "complete"
        },
    )


    assert (
        api.available(
            "analysis"
        )
        is True
    )



def test_execute():

    api = RuntimeIntelligenceAPI()


    api.register(
        "investigation",
        lambda ctx: {
            "id":
                ctx.investigation_id
        },
    )


    result = api.execute(
        "investigation",
        "INC-001",
    )


    assert (
        result["id"]
        ==
        "INC-001"
    )



def test_missing():

    api = RuntimeIntelligenceAPI()


    result = api.execute(
        "unknown",
        "INC-001",
    )


    assert result is None



def test_status():

    api = RuntimeIntelligenceAPI()


    result = api.status()


    assert "requests" in result