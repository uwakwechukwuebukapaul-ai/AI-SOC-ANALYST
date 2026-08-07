"""
Tests for Runtime Policy Engine
"""

from services.intelligence.runtime.policy_engine import (
    PolicyEngine,
)



def test_policy_init():

    engine = PolicyEngine()

    assert engine.size() == 0



def test_register_policy():

    engine = PolicyEngine()


    def allow(context):
        return True


    engine.register_policy(
        "allow_all",
        allow,
    )


    assert engine.exists(
        "allow_all"
    )



def test_policy_allow():

    engine = PolicyEngine()


    engine.register_policy(
        "allow",
        lambda ctx: True,
    )


    result = engine.evaluate(
        {
            "action": "scan"
        }
    )


    assert result is True



def test_policy_deny():

    engine = PolicyEngine()


    engine.register_policy(
        "deny",
        lambda ctx: False,
    )


    result = engine.evaluate(
        {}
    )


    assert result is False



def test_remove_policy():

    engine = PolicyEngine()


    engine.register_policy(
        "test",
        lambda ctx: True,
    )


    engine.remove_policy(
        "test"
    )


    assert engine.exists(
        "test"
    ) is False



def test_clear():

    engine = PolicyEngine()


    engine.register_policy(
        "test",
        lambda ctx: True,
    )


    engine.clear()


    assert engine.size() == 0



def test_to_dict():

    engine = PolicyEngine()


    engine.register_policy(
        "security_check",
        lambda ctx: True,
    )


    data = engine.to_dict()


    assert data["policy_count"] == 1