from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class OrchestrationContext:

    case_id: str

    alert: Dict[str, Any] = field(default_factory=dict)

    evidence: List[Any] = field(default_factory=list)

    findings: List[Any] = field(default_factory=list)

    agent_results: Dict[str, Any] = field(default_factory=dict)

    shared_data: Dict[str, Any] = field(default_factory=dict)


    def add_result(self, agent_name, result):
        self.agent_results[agent_name] = result


    def add_finding(self, finding):
        self.findings.append(finding)