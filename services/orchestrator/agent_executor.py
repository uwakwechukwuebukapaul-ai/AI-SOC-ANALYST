"""
Sentinel DNA
Enterprise Agent Execution Engine

Responsible for executing registered agents safely
inside the investigation orchestration lifecycle.

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional


def utc_now():
    return datetime.now(timezone.utc)


@dataclass
class AgentExecutionResult:
    """
    Result returned after agent execution.
    """

    agent_name: str

    success: bool = False

    output: Dict[str, Any] = field(default_factory=dict)

    error: Optional[str] = None

    started_at: datetime = field(default_factory=utc_now)

    completed_at: Optional[datetime] = None

    def complete(self):
        self.completed_at = utc_now()


class AgentExecutor:
    """
    Enterprise execution layer for autonomous agents.

    Responsibilities:
    - Execute agents
    - Capture results
    - Handle failures
    - Track execution lifecycle
    """

    def __init__(self):

        self.executions = []


    def execute(
        self,
        agent,
        context,
    ) -> AgentExecutionResult:
        """
        Execute an agent against investigation context.
        """

        result = AgentExecutionResult(
            agent_name=agent.name
        )

        try:

            output = agent.run(context)

            result.success = True

            result.output = (
                output
                if isinstance(output, dict)
                else {
                    "result": output
                }
            )


        except Exception as error:

            result.success = False

            result.error = str(error)


        finally:

            result.complete()

            self.executions.append(result)


        return result


    def get_execution_history(self):
        """
        Return previous executions.
        """

        return self.executions


    def clear_history(self):
        """
        Clear execution history.
        """

        self.executions.clear()