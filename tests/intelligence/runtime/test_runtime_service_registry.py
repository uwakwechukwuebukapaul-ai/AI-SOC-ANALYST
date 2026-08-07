"""
Runtime Service Registry Tests
"""

from services.intelligence.runtime.runtime_service_registry import (
    RuntimeServiceRegistry,
)



class FakeService:
    pass



def test_init():

    registry = RuntimeServiceRegistry()

    assert (
        registry.count()
        ==
        0
    )



def test_register():

    registry = RuntimeServiceRegistry()

    service = FakeService()


    registry.register(
        "threat_intelligence",
        service,
    )


    assert (
        registry.exists(
            "threat_intelligence"
        )
        is True
    )



def test_get():

    registry = RuntimeServiceRegistry()

    service = FakeService()


    registry.register(
        "analysis",
        service,
    )


    result = registry.get(
        "analysis"
    )


    assert (
        result
        is
        service
    )



def test_unregister():

    registry = RuntimeServiceRegistry()


    registry.register(
        "service",
        FakeService(),
    )


    registry.unregister(
        "service"
    )


    assert (
        registry.exists(
            "service"
        )
        is False
    )



def test_clear():

    registry = RuntimeServiceRegistry()


    registry.register(
        "service",
        FakeService(),
    )


    registry.clear()


    assert (
        registry.count()
        ==
        0
    )



def test_status():

    registry = RuntimeServiceRegistry()


    result = registry.status()


    assert "services" in result

    assert "count" in result