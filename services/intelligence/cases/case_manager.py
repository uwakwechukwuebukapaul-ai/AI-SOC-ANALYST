"""
Sentinel DNA Case Manager

Enterprise investigation case lifecycle.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.cases.case_timeline import (
    CaseTimeline,
)

from services.intelligence.cases.evidence_graph import (
    EvidenceGraph,
)

from services.intelligence.cases.investigation_state import (
    InvestigationState,
)


class CaseManager:

    def __init__(self):

        self.cases: dict[str, dict[str, Any]] = {}


    def create_case(
        self,
        case_id: str,
        alert: dict[str, Any],
    ):

        case = {

            "case_id": case_id,

            "alert": alert,

            "state": InvestigationState.CREATED.value,

            "timeline": CaseTimeline(),

            "evidence": EvidenceGraph(),

        }


        self.cases[case_id] = case


        case["timeline"].add_event(
            "case_created",
            "Investigation case created",
        )


        return case



    def get_case(
        self,
        case_id: str,
    ):

        return self.cases.get(
            case_id
        )



    def update_state(
        self,
        case_id: str,
        state: InvestigationState,
    ):

        case = self.cases.get(
            case_id
        )


        if not case:

            raise ValueError(
                "Case not found"
            )


        case["state"] = state.value


        case["timeline"].add_event(
            "state_changed",
            f"Case moved to {state.value}",
        )


        return case