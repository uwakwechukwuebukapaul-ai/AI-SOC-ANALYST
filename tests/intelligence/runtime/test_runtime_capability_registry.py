"""
Runtime Capability Registry Tests
"""

from services.intelligence.runtime.runtime_capability_registry import (
    RuntimeCapabilityRegistry,
)


def test_register():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "ioc_enrichment",
        "ThreatIntelAgent",
    )

    assert registry.count() == 1


def test_get():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "mitre_mapping",
        "MitreEngine",
    )

    assert (
        registry.get(
            "mitre_mapping"
        )["provider"]
        == "MitreEngine"
    )


def test_exists():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "email_analysis",
        "EmailAgent",
    )

    assert registry.exists(
        "email_analysis"
    )


def test_remove():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "lookup",
        "IntelEngine",
    )

    registry.remove(
        "lookup"
    )

    assert registry.exists(
        "lookup"
    ) is False


def test_list():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "a",
        "EngineA",
    )

    registry.register(
        "b",
        "EngineB",
    )

    assert len(
        registry.list_capabilities()
    ) == 2


def test_clear():

    registry = RuntimeCapabilityRegistry()

    registry.register(
        "x",
        "Engine",
    )

    registry.clear()

    assert registry.count() == 0


def test_status():

    registry = RuntimeCapabilityRegistry()

    result = registry.status()

    assert "count" in result

    assert "capabilities" in result