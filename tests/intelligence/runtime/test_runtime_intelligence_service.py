"""
Runtime Intelligence Service Tests
"""

from services.intelligence.runtime.runtime_intelligence_service import (
    RuntimeIntelligenceService,
)

from services.intelligence.runtime.runtime_intelligence_context import (
    RuntimeIntelligenceContext,
)



def test_init():

    service = RuntimeIntelligenceService()

    assert (
        service.requests
        ==
        0
    )


def test_register():

    service = RuntimeIntelligenceService()


    service.register_capability(
        "ioc_analysis",
        lambda ctx: {
            "ioc":
                True
        },
    )


    assert (
        service.available(
            "ioc_analysis"
        )
        is True
    )


def test_investigate():

    service = RuntimeIntelligenceService()


    service.register_capability(
        "analysis",
        lambda ctx: {
            "case":
                ctx.investigation_id
        },
    )


    context = RuntimeIntelligenceContext(
        "INC-100"
    )


    result = service.investigate(
        "analysis",
        context,
    )


    assert (
        result["case"]
        ==
        "INC-100"
    )



def test_missing():

    service = RuntimeIntelligenceService()


    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    result = service.investigate(
        "unknown",
        context,
    )


    assert result is None



def test_clear():

    service = RuntimeIntelligenceService()


    service.register_capability(
        "test",
        lambda ctx: True,
    )


    service.clear()


    assert (
        service.available(
            "test"
        )
        is False
    )



def test_status():

    service = RuntimeIntelligenceService()


    result = service.status()


    assert "requests" in result

    assert "pipeline" in result