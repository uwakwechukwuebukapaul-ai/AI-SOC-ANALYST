"""
Sentinel DNA
Enterprise Investigation State Machine

Defines investigation lifecycle states and validates
state transitions.

Author: Sentinel DNA
"""

from enum import Enum


class InvestigationState(str, Enum):
    NEW = "NEW"

    INGESTING = "INGESTING"

    IOC_EXTRACTION = "IOC_EXTRACTION"

    THREAT_INTEL = "THREAT_INTEL"

    EVIDENCE_COLLECTION = "EVIDENCE_COLLECTION"

    MITRE_MAPPING = "MITRE_MAPPING"

    AI_ANALYSIS = "AI_ANALYSIS"

    RECOMMENDATIONS = "RECOMMENDATIONS"

    RESPONSE = "RESPONSE"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    TERMINATED = "TERMINATED"


VALID_TRANSITIONS = {
    InvestigationState.NEW: [
        InvestigationState.INGESTING,
        InvestigationState.TERMINATED,
    ],

    InvestigationState.INGESTING: [
        InvestigationState.IOC_EXTRACTION,
        InvestigationState.FAILED,
    ],

    InvestigationState.IOC_EXTRACTION: [
        InvestigationState.THREAT_INTEL,
        InvestigationState.FAILED,
    ],

    InvestigationState.THREAT_INTEL: [
        InvestigationState.EVIDENCE_COLLECTION,
        InvestigationState.FAILED,
    ],

    InvestigationState.EVIDENCE_COLLECTION: [
        InvestigationState.MITRE_MAPPING,
        InvestigationState.FAILED,
    ],

    InvestigationState.MITRE_MAPPING: [
        InvestigationState.AI_ANALYSIS,
        InvestigationState.FAILED,
    ],

    InvestigationState.AI_ANALYSIS: [
        InvestigationState.RECOMMENDATIONS,
        InvestigationState.FAILED,
    ],

    InvestigationState.RECOMMENDATIONS: [
        InvestigationState.RESPONSE,
        InvestigationState.FAILED,
    ],

    InvestigationState.RESPONSE: [
        InvestigationState.COMPLETED,
        InvestigationState.FAILED,
    ],

    InvestigationState.FAILED: [
        InvestigationState.INGESTING,
        InvestigationState.TERMINATED,
    ],

    InvestigationState.COMPLETED: [],

    InvestigationState.TERMINATED: [],
}


class InvestigationStateMachine:
    """
    Validates workflow transitions for investigations.
    """

    def __init__(self):
        self.current_state = InvestigationState.NEW

    def get_state(self) -> InvestigationState:
        return self.current_state

    def can_transition(self, new_state: InvestigationState) -> bool:
        return new_state in VALID_TRANSITIONS[self.current_state]

    def transition(self, new_state: InvestigationState) -> None:
        if not self.can_transition(new_state):
            raise ValueError(
                f"Invalid transition: "
                f"{self.current_state} -> {new_state}"
            )

        self.current_state = new_state

    def reset(self):
        self.current_state = InvestigationState.NEW

    def is_complete(self):
        return self.current_state == InvestigationState.COMPLETED

    def is_failed(self):
        return self.current_state == InvestigationState.FAILED

    def is_terminated(self):
        return self.current_state == InvestigationState.TERMINATED