"""
Runtime Policy Registry Tests
"""

from services.intelligence.runtime.runtime_policy_registry import (
    RuntimePolicyRegistry,
)



def test_init():

    registry = RuntimePolicyRegistry()

    assert (
        registry.count()
        ==
        0
    )



def test_register():

    registry = RuntimePolicyRegistry()


    registry.register(
        "allow_scan",
        lambda ctx: True,
    )


    assert (
        registry.exists(
            "allow_scan"
        )
        is True
    )



def test_evaluate_success():

    registry = RuntimePolicyRegistry()


    registry.register(
        "security_check",
        lambda ctx: True,
    )


    result = registry.evaluate(
        "security_check",
        {},
    )


    assert result is True



def test_evaluate_failure():

    registry = RuntimePolicyRegistry()


    registry.register(
        "blocked_action",
        lambda ctx: False,
    )


    result = registry.evaluate(
        "blocked_action",
        {},
    )


    assert result is False



def test_missing_policy():

    registry = RuntimePolicyRegistry()


    result = registry.evaluate(
        "missing",
        {},
    )


    assert result is None



def test_remove():

    registry = RuntimePolicyRegistry()


    registry.register(
        "test",
        lambda ctx: True,
    )


    registry.remove(
        "test"
    )


    assert (
        registry.exists(
            "test"
        )
        is False
    )



def test_clear():

    registry = RuntimePolicyRegistry()


    registry.register(
        "test",
        lambda ctx: True,
    )


    registry.clear()


    assert (
        registry.count()
        ==
        0
    )



def test_status():

    registry = RuntimePolicyRegistry()


    result = registry.status()


    assert "policies" in result

    assert "count" in result