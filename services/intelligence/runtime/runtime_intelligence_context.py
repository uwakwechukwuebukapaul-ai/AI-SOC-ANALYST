"""
Sentinel DNA Runtime Intelligence Context

Shared execution context for intelligence workflows.

Responsibilities:

- store investigation data
- maintain runtime metadata
- share intelligence state
- provide context snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeIntelligenceContext:
    """
    Shared runtime intelligence context.
    """

    investigation_id: str

    evidence: list[dict[str, Any]] = field(
        default_factory=list
    )

    iocs: list[dict[str, Any]] = field(
        default_factory=list
    )

    mitre: list[dict[str, Any]] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def add_evidence(
        self,
        evidence: dict[str, Any],
    ) -> None:
        """
        Add evidence item.
        """

        self.evidence.append(
            evidence
        )



    def add_ioc(
        self,
        ioc: dict[str, Any],
    ) -> None:
        """
        Add IOC.
        """

        self.iocs.append(
            ioc
        )



    def add_mitre(
        self,
        technique: dict[str, Any],
    ) -> None:
        """
        Add MITRE mapping.
        """

        self.mitre.append(
            technique
        )



    def update_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Update metadata.
        """

        self.metadata[key] = value



    def status(self) -> dict[str, Any]:
        """
        Context summary.
        """

        return {
            "investigation_id":
                self.investigation_id,

            "evidence_count":
                len(self.evidence),

            "ioc_count":
                len(self.iocs),

            "mitre_count":
                len(self.mitre),

            "metadata":
                self.metadata,
        }