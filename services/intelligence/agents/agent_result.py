from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class AgentExecutionStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    RUNNING = "running"
    PENDING = "pending"


@dataclass
class AgentResult:
    agent_name: str

    status: AgentExecutionStatus = AgentExecutionStatus.SUCCESS

    confidence: float = 0.0

    findings: List[Any] = field(default_factory=list)

    recommendations: List[Any] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)

    artifacts: Dict[str, Any] = field(default_factory=dict)

    metrics: Dict[str, Any] = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)


    def successful(self) -> bool:
        """
        Returns True when the agent completed successfully.
        """

        return self.status == AgentExecutionStatus.SUCCESS


    def failed(self) -> bool:
        """
        Returns True when the agent execution failed.
        """

        return self.status == AgentExecutionStatus.FAILED


    def add_finding(self, finding):
        self.findings.append(finding)


    def add_recommendation(self, recommendation):
        self.recommendations.append(recommendation)


    def add_artifact(self, name: str, value: Any):
        self.artifacts[name] = value


    def add_metric(self, name: str, value: Any):
        self.metrics[name] = value


    def add_error(self, error: str):
        self.errors.append(error)
        self.status = AgentExecutionStatus.FAILED


    def summary(self):
        return {
            "agent_name": self.agent_name,
            "status": self.status.value,
            "confidence": self.confidence,
            "findings": len(self.findings),
            "recommendations": len(self.recommendations),
            "artifacts": len(self.artifacts),
            "metrics": self.metrics,
            "errors": len(self.errors),
        }


    def to_dict(self):
        return {
            "agent_name": self.agent_name,
            "status": self.status.value,
            "confidence": self.confidence,
            "findings": self.findings,
            "recommendations": self.recommendations,
            "errors": self.errors,
            "artifacts": self.artifacts,
            "metrics": self.metrics,
            "metadata": self.metadata,
        }