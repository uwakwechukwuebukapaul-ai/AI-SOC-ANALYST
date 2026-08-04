"""
Tests for Sentinel DNA Agent Executor
"""

import pytest

from services.orchestrator.agent_executor import (
    AgentExecutor,
)


class MockAgent:

    name = "test_agent"


    def run(self, context):

        return {
            "status": "completed",
            "finding": "malware detected",
        }



class FailingAgent:

    name = "failing_agent"


    def run(self, context):

        raise Exception(
            "agent failure"
        )


def test_agent_execution_success():

    executor = AgentExecutor()

    result = executor.execute(
        MockAgent(),
        {}
    )

    assert result.success is True

    assert result.agent_name == "test_agent"

    assert result.output["status"] == "completed"



def test_agent_execution_failure():

    executor = AgentExecutor()

    result = executor.execute(
        FailingAgent(),
        {}
    )

    assert result.success is False

    assert result.error == "agent failure"



def test_execution_history():

    executor = AgentExecutor()

    executor.execute(
        MockAgent(),
        {}
    )

    history = executor.get_execution_history()

    assert len(history) == 1



def test_clear_execution_history():

    executor = AgentExecutor()

    executor.execute(
        MockAgent(),
        {}
    )

    executor.clear_history()

    assert len(
        executor.get_execution_history()
    ) == 0



def test_multiple_agent_executions():

    executor = AgentExecutor()

    executor.execute(
        MockAgent(),
        {}
    )

    executor.execute(
        MockAgent(),
        {}
    )

    assert len(
        executor.get_execution_history()
    ) == 2