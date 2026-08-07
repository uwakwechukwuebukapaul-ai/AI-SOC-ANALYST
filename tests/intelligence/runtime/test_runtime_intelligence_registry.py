"""
Runtime Intelligence Registry Tests
"""

from services.intelligence.runtime.runtime_intelligence_registry import (
    RuntimeIntelligenceRegistry,
)



def test_init():

    registry = RuntimeIntelligenceRegistry()

    assert (
        registry.count()
        ==
        0
    )



def test_register():

    registry = RuntimeIntelligenceRegistry()


    registry.register(
        "threat_engine",
        [
            "ioc_lookup",
            "reputation",
        ],
    )


    assert (
        registry.exists(
            "threat_engine"
        )
        is True
    )



def test_find_provider():

    registry = RuntimeIntelligenceRegistry()


    registry.register(
        "investigation_engine",
        [
            "investigate",
        ],
    )


    result = registry.find_provider(
        "investigate"
    )


    assert (
        result
        ==
        "investigation_engine"
    )



def test_unregister():

    registry = RuntimeIntelligenceRegistry()


    registry.register(
        "module",
        [],
    )


    registry.unregister(
        "module"
    )


    assert (
        registry.exists(
            "module"
        )
        is False
    )



def test_clear():

    registry = RuntimeIntelligenceRegistry()


    registry.register(
        "module",
        [],
    )


    registry.clear()


    assert (
        registry.count()
        ==
        0
    )



def test_status():

    registry = RuntimeIntelligenceRegistry()


    result = registry.status()


    assert "modules" in result

    assert "registered" in result