"""
Runtime Intelligence Facade Tests
"""

from services.intelligence.runtime.runtime_intelligence_facade import (
    RuntimeIntelligenceFacade,
)


def test_init():

    facade = RuntimeIntelligenceFacade()

    assert facade.controller is not None



def test_register():

    facade = RuntimeIntelligenceFacade()


    facade.register_capability(
        "ioc_analysis",
        lambda ctx: {
            "ioc":
                True
        },
    )


    result = facade.controller.api.available(
        "ioc_analysis"
    )


    assert result is True



def test_execute():

    facade = RuntimeIntelligenceFacade()


    facade.register_capability(
        "investigation",
        lambda ctx: {
            "case":
                ctx.investigation_id
        },
    )


    result = facade.execute(
        "investigation",
        "INC-100",
    )


    assert (
        result["success"]
        is True
    )

    assert (
        result["result"]["case"]
        ==
        "INC-100"
    )



def test_missing():

    facade = RuntimeIntelligenceFacade()


    result = facade.execute(
        "unknown",
        "INC-001",
    )


    assert (
        result["success"]
        is False
    )



def test_status():

    facade = RuntimeIntelligenceFacade()


    result = facade.status()


    assert "requests" in result