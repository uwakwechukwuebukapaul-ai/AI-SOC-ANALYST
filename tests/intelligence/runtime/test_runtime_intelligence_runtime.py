"""
Runtime Intelligence Runtime Tests
"""

from services.intelligence.runtime.runtime_intelligence_runtime import (
    RuntimeIntelligenceRuntime,
)



def test_init():

    runtime = RuntimeIntelligenceRuntime()

    assert (
        runtime.running
        is False
    )



def test_start():

    runtime = RuntimeIntelligenceRuntime()

    runtime.start()


    assert (
        runtime.running
        is True
    )



def test_stop():

    runtime = RuntimeIntelligenceRuntime()

    runtime.start()

    runtime.stop()


    assert (
        runtime.running
        is False
    )



def test_register():

    runtime = RuntimeIntelligenceRuntime()


    runtime.register(
        "analysis",
        lambda ctx: {
            "ok":
                True
        },
    )


    assert (
        runtime.facade.controller.api.available(
            "analysis"
        )
        is True
    )



def test_execute():

    runtime = RuntimeIntelligenceRuntime()


    runtime.register(
        "investigation",
        lambda ctx: {
            "id":
                ctx.investigation_id
        },
    )


    result = runtime.execute(
        "investigation",
        "INC-001",
    )


    assert (
        result["success"]
        is True
    )



def test_health():

    runtime = RuntimeIntelligenceRuntime()


    result = runtime.health()


    assert "running" in result

    assert "intelligence" in result