from services.orchestrator.agent_governance import AgentGovernance


def test_register_policy():

    governance = AgentGovernance()

    policy = governance.register_policy(
        agent_name="response_agent",
        permissions=[
            "isolate_host",
            "block_ip",
        ],
        autonomy_level=3,
        approval_required=False,
    )

    assert policy.agent_name == "response_agent"

    assert policy.autonomy_level == 3



def test_permission_check():

    governance = AgentGovernance()

    governance.register_policy(
        "ioc_agent",
        [
            "lookup_ioc",
        ],
    )

    assert governance.has_permission(
        "ioc_agent",
        "lookup_ioc",
    )



def test_execute_allowed_action():

    governance = AgentGovernance()

    governance.register_policy(
        "response_agent",
        [
            "containment",
        ],
        autonomy_level=3,
    )

    result = governance.can_execute(
        "response_agent",
        "containment",
    )

    assert result["allowed"] is True



def test_execute_blocked_action():

    governance = AgentGovernance()

    governance.register_policy(
        "analysis_agent",
        [
            "read_logs",
        ],
    )

    result = governance.can_execute(
        "analysis_agent",
        "disable_user",
    )

    assert result["allowed"] is False



def test_disable_agent():

    governance = AgentGovernance()

    governance.register_policy(
        "hunter_agent",
        [
            "hunt",
        ],
    )

    policy = governance.disable_agent(
        "hunter_agent"
    )

    assert policy.status == "DISABLED"