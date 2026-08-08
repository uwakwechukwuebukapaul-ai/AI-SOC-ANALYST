"""
Sentinel DNA Investigation Report Model

Normalized intelligence output
for analysts and automation systems.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class InvestigationReport:

    case_id: str

    severity: str = "UNKNOWN"

    risk_score: float = 0.0


    findings: list[dict[str, Any]] = field(
        default_factory=list
    )


    iocs: list[dict[str, Any]] = field(
        default_factory=list
    )


    recommendations: list[str] = field(
        default_factory=list
    )


    agent_results: dict[str, Any] = field(
        default_factory=dict
    )


    metadata: dict[str, Any] = field(
        default_factory=dict
    )