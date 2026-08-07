from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class OrchestrationResult:
    """
    Result returned after an investigation workflow execution.
    """

    plan_name: str

    success: bool = True

    agents_executed: List[str] = field(
        default_factory=list
    )

    results: Dict[str, Any] = field(
        default_factory=dict
    )

    errors: List[str] = field(
        default_factory=list
    )


    def add_agent_result(
        self,
        agent_name: str,
        result: Any
    ):
        self.agents_executed.append(agent_name)
        self.results[agent_name] = result


    def add_error(
        self,
        error: str
    ):
        self.errors.append(error)
        self.success = False


    def summary(self):

        return {
            "plan_name": self.plan_name,
            "success": self.success,
            "agents": self.agents_executed,
            "errors": self.errors,
            "result_count": len(self.results),
        }


    def to_dict(self):

        return {
            "plan_name": self.plan_name,
            "success": self.success,
            "agents_executed": self.agents_executed,
            "results": self.results,
            "errors": self.errors,
        }