"""
Runtime Policy Engine Tests
"""

from services.intelligence.runtime.runtime_policy_engine import (
    RuntimePolicyEngine,
)



def test_init():

    engine = RuntimePolicyEngine()

    assert (
        engine.count()
        ==
        0
    )



def test_register():

    engine = RuntimePolicyEngine()


    engine.register(
        "allow_low_risk",
        lambda ctx: ctx["risk"] == "low",
    )


    assert (
        engine.exists(
            "allow_low_risk"
        )
        is True
    )



def test_allow_policy():

    engine = RuntimePolicyEngine()


    engine.register(
        "safe",
        lambda ctx: True,
    )


    result = engine.evaluate(
        "safe",
        {},
    )


    assert result is True



def test_deny_policy():

    engine = RuntimePolicyEngine()


    engine.register(
        "blocked",
        lambda ctx: False,
    )


    result = engine.evaluate(
        "blocked",
        {},
    )


    assert result is False



def test_missing_policy():

    engine = RuntimePolicyEngine()


    result = engine.evaluate(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    engine = RuntimePolicyEngine()


    engine.register(
        "test",
        lambda x: True,
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