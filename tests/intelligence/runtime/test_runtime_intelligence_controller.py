"""
Runtime Intelligence Controller Tests
"""

from services.intelligence.runtime.runtime_intelligence_controller import (
    RuntimeIntelligenceController,
)



def test_init():

    controller = RuntimeIntelligenceController()

    assert controller.api is not None



def test_register():

    controller = RuntimeIntelligenceController()


    controller.register(
        "analysis",
        lambda ctx: {
            "ok": True
        },
    )


    assert (
        controller.api.available(
            "analysis"
        )
        is True
    )



def test_investigate():

    controller = RuntimeIntelligenceController()


    controller.register(
        "analysis",
        lambda ctx: {
            "id":
                ctx.investigation_id
        },
    )


    response = controller.investigate(
        {
            "capability":
                "analysis",

            "investigation_id":
                "INC-001",
        }
    )


    assert (
        response["success"]
        is True
    )

    assert (
        response["result"]["id"]
        ==
        "INC-001"
    )



def test_invalid_request():

    controller = RuntimeIntelligenceController()


    response = controller.investigate(
        {}
    )


    assert (
        response["success"]
        is False
    )



def test_missing_capability():

    controller = RuntimeIntelligenceController()


    response = controller.investigate(
        {
            "capability":
                "unknown",

            "investigation_id":
                "INC-001",
        }
    )


    assert (
        response["success"]
        is False
    )



def test_status():

    controller = RuntimeIntelligenceController()


    result = controller.status()


    assert "requests" in result