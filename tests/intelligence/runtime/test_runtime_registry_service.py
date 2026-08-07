"""
Runtime Registry Service Tests
"""

from services.intelligence.runtime.runtime_registry_service import (
    RuntimeRegistryService,
)



def test_service_init():

    service = RuntimeRegistryService()

    assert (
        service.registry
        is not None
    )



def test_register_capability():

    service = RuntimeRegistryService()


    handler = lambda x: x


    service.register_capability(
        "analysis",
        handler,
    )


    assert (
        service.get_capability(
            "analysis"
        )
        == handler
    )



def test_register_handler():

    service = RuntimeRegistryService()


    handler = lambda x: x


    service.register_handler(
        "test",
        handler,
    )


    result = (
        service.registry
        .to_dict()
    )


    assert (
        "test"
        in result["handlers"]
    )



def test_register_agent():

    service = RuntimeRegistryService()


    service.register_agent(
        "ThreatAgent",
        {
            "version": "1.0"
        },
    )


    result = service.status()


    assert (
        "ThreatAgent"
        in result["agents"]
    )



def test_clear():

    service = RuntimeRegistryService()

    service.register_agent(
        "agent",
        {}
    )


    service.clear()


    result = service.status()


    assert (
        result["agents"]
        == []
    )



def test_status():

    service = RuntimeRegistryService()

    result = service.status()

    assert isinstance(
        result,
        dict
    )