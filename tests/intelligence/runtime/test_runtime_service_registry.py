"""
Runtime Service Registry Tests
"""

from services.intelligence.runtime.runtime_service_registry import (
    RuntimeServiceRegistry,
)


class FakeService:
    pass


def test_register():

    registry = RuntimeServiceRegistry()

    registry.register(
        "database",
        FakeService(),
    )

    assert registry.count() == 1


def test_resolve():

    registry = RuntimeServiceRegistry()

    service = FakeService()

    registry.register(
        "database",
        service,
    )

    assert registry.resolve(
        "database"
    ) is service


def test_exists():

    registry = RuntimeServiceRegistry()

    registry.register(
        "intel",
        FakeService(),
    )

    assert registry.exists(
        "intel"
    )


def test_remove():

    registry = RuntimeServiceRegistry()

    registry.register(
        "cache",
        FakeService(),
    )

    registry.remove(
        "cache"
    )

    assert registry.exists(
        "cache"
    ) is False


def test_list_services():

    registry = RuntimeServiceRegistry()

    registry.register(
        "a",
        FakeService(),
    )

    registry.register(
        "b",
        FakeService(),
    )

    assert len(
        registry.list_services()
    ) == 2


def test_clear():

    registry = RuntimeServiceRegistry()

    registry.register(
        "x",
        FakeService(),
    )

    registry.clear()

    assert registry.count() == 0


def test_status():

    registry = RuntimeServiceRegistry()

    result = registry.status()

    assert "count" in result

    assert "services" in result