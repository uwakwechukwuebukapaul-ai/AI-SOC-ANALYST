"""
Runtime Bootstrap Tests
"""

from services.intelligence.runtime.runtime_bootstrap import (
    initialize_runtime,
    get_runtime,
    register_capability,
)



def test_initialize():

    runtime = initialize_runtime()


    assert (
        runtime.running
        is True
    )



def test_singleton():

    first = get_runtime()

    second = get_runtime()


    assert (
        first
        is
        second
    )



def test_register():

    register_capability(
        "analysis",
        lambda ctx: {
            "ok":
                True
        },
    )


    runtime = get_runtime()


    assert (
        runtime.facade.controller.api.available(
            "analysis"
        )
        is True
    )



def test_health():

    runtime = get_runtime()


    result = runtime.health()


    assert "running" in result