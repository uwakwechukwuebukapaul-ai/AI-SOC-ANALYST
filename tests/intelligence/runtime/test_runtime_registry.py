from services.intelligence.runtime.runtime_registry import RuntimeRegistry


def test_default_registry():

    registry = RuntimeRegistry()

    assert registry.agents == {}
    assert registry.handlers == {}
    assert registry.capabilities == {}


def test_register_agent():

    registry = RuntimeRegistry()

    agent = object()

    registry.register_agent(
        "analyst",
        agent
    )

    assert registry.get_agent(
        "analyst"
    ) == agent


def test_register_handler():

    registry = RuntimeRegistry()

    handler = object()

    registry.register_handler(
        "email_handler",
        handler
    )

    assert registry.get_handler(
        "email_handler"
    ) == handler


def test_register_capability():

    registry = RuntimeRegistry()

    registry.register_capability(
        "investigation",
        True
    )

    assert registry.get_capability(
        "investigation"
    ) is True


def test_clear():

    registry = RuntimeRegistry()

    registry.register_agent(
        "test_agent",
        object()
    )

    registry.clear()

    assert registry.agents == {}


def test_to_dict():

    registry = RuntimeRegistry()

    result = registry.to_dict()

    assert "agents" in result
    assert "handlers" in result
    assert "capabilities" in result