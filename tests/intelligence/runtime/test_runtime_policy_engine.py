"""
Runtime Policy Engine Tests
"""

from services.intelligence.runtime.runtime_policy_engine import (
    RuntimePolicyEngine,
)



def test_init():

    engine = RuntimePolicyEngine()

    assert (
        engine.evaluations
        ==
        0
    )



def test_register():

    engine = RuntimePolicyEngine()


    engine.register(
        "allow_admin",
        lambda ctx: True,
    )


    assert (
        engine.exists(
            "allow_admin"
        )
        is True
    )



def test_evaluate_allow():

    engine = RuntimePolicyEngine()


    engine.register(
        "allow",
        lambda ctx: True,
    )


    result = engine.evaluate(
        "allow",
        {},
    )


    assert (
        result
        is True
    )



def test_evaluate_deny():

    engine = RuntimePolicyEngine()


    engine.register(
        "deny",
        lambda ctx: False,
    )


    result = engine.evaluate(
        "deny",
        {},
    )


    assert (
        result
        is False
    )



def test_missing_policy():

    engine = RuntimePolicyEngine()


    result = engine.evaluate(
        "missing",
        {},
    )


    assert (
        result
        is False
    )



def test_clear():

    engine = RuntimePolicyEngine()


    engine.register(
        "test",
        lambda ctx: True,
    )


    engine.clear()


    assert (
        engine.exists(
            "test"
        )
        is False
    )



def test_status():

    engine = RuntimePolicyEngine()


    result = engine.status()


    assert "policies" in result

    assert "evaluations" in result