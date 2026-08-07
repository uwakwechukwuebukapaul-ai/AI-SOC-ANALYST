"""
Runtime Platform Orchestrator Tests
"""

from services.intelligence.runtime.runtime_platform_orchestrator import (
    RuntimePlatformOrchestrator,
)



def test_init():

    platform = RuntimePlatformOrchestrator()

    assert (
        platform.running
        is False
    )



def test_start():

    platform = RuntimePlatformOrchestrator()


    platform.start()


    assert (
        platform.running
        is True
    )



def test_stop():

    platform = RuntimePlatformOrchestrator()


    platform.start()

    platform.stop()


    assert (
        platform.running
        is False
    )



def test_process():

    platform = RuntimePlatformOrchestrator()


    platform.soc.detection.register_rule(
        "test",
        lambda event: {
            "detected":
                True
        },
    )


    platform.start()


    result = platform.process(
        "test",
        {},
    )


    assert (
        result["detected"]
        is True
    )



def test_health():

    platform = RuntimePlatformOrchestrator()


    result = platform.health()


    assert "running" in result

    assert "events" in result



def test_clear():

    platform = RuntimePlatformOrchestrator()


    platform.events = 5


    platform.clear()


    assert (
        platform.events
        ==
        0
    )



def test_status():

    platform = RuntimePlatformOrchestrator()


    result = platform.status()


    assert "running" in result

    assert "soc" in result