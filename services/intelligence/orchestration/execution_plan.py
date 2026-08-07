from dataclasses import dataclass, field
from typing import List


@dataclass
class ExecutionPlan:

    name: str

    agents: List[str] = field(default_factory=list)