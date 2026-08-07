"""
Runtime Intelligence Pipeline Tests
"""

from services.intelligence.runtime.runtime_intelligence_pipeline import (
    RuntimeIntelligencePipeline,
)

from services.intelligence.runtime.runtime_intelligence_context import (
    RuntimeIntelligenceContext,
)



def test_init():

    pipeline = RuntimeIntelligencePipeline()

    assert (
        pipeline.executions
        ==
        0
    )



def test_register():

    pipeline = RuntimeIntelligencePipeline()


    pipeline.register(
        "analysis",
        lambda ctx: {
            "done": True
        },
    )


    assert (
        pipeline.available(
            "analysis"
        )
        is True
    )



def test_execute():

    pipeline = RuntimeIntelligencePipeline()


    pipeline.register(
        "analysis",
        lambda ctx: {
            "id":
                ctx.investigation_id
        },
    )


    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    result = pipeline.execute(
        "analysis",
        context,
    )


    assert (
        result["id"]
        ==
        "INC-001"
    )



def test_missing():

    pipeline = RuntimeIntelligencePipeline()


    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    result = pipeline.execute(
        "unknown",
        context,
    )


    assert result is None



def test_clear():

    pipeline = RuntimeIntelligencePipeline()


    pipeline.register(
        "test",
        lambda ctx: True,
    )


    pipeline.clear()


    assert (
        pipeline.available(
            "test"
        )
        is False
    )



def test_status():

    pipeline = RuntimeIntelligencePipeline()


    result = pipeline.status()


    assert "executions" in result

    assert "router" in result