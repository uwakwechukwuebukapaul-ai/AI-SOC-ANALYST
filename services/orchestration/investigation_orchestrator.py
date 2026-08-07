"""
Sentinel DNA unified investigation orchestrator.

Coordinates existing intelligence services through a common
investigation lifecycle.
"""

from __future__ import annotations

from typing import Any, Callable

from .execution_trace import ExecutionTrace
from .investigation_context import InvestigationContext
from .workflow_state import WorkflowState


StepHandler = Callable[
    [InvestigationContext],
    dict[str, Any] | None,
]


class InvestigationOrchestrator:
    """
    Execute a deterministic investigation workflow.

    Business logic remains inside individual intelligence services.
    This class is responsible only for orchestration and state flow.
    """

    DEFAULT_STEPS = (
        "analysis",
        "enrichment",
        "decision",
        "response",
    )

    def __init__(self) -> None:
        self._handlers: dict[str, StepHandler] = {}
        self.trace = ExecutionTrace()

    def register_step(
        self,
        name: str,
        handler: StepHandler,
    ) -> None:
        """Register a workflow step."""

        if not name or not name.strip():
            raise ValueError("Step name is required.")

        if not callable(handler):
            raise TypeError("Step handler must be callable.")

        self._handlers[name] = handler

    def registered_steps(self) -> list[str]:
        """Return registered workflow steps."""

        return list(self._handlers)

    def run(
        self,
        *,
        case_id: str,
        alert: dict[str, Any],
    ) -> dict[str, Any]:
        """Execute the unified investigation workflow."""

        context = InvestigationContext(
            case_id=case_id,
            alert=alert,
        )

        state = WorkflowState.CREATED

        self.trace.record(
            step="investigation",
            status=state.value,
            details={"case_id": case_id},
        )

        try:
            for step_name in self.DEFAULT_STEPS:
                handler = self._handlers.get(step_name)

                if handler is None:
                    continue

                state = self._state_for_step(step_name)

                self.trace.record(
                    step=step_name,
                    status="started",
                )

                context.add_timeline_event(
                    f"{step_name}_started"
                )

                result = handler(context)

                if result:
                    self._apply_result(
                        context,
                        step_name,
                        result,
                    )

                context.add_timeline_event(
                    f"{step_name}_completed"
                )

                self.trace.record(
                    step=step_name,
                    status="completed",
                    details=result or {},
                )

            state = WorkflowState.COMPLETED

            context.add_timeline_event(
                "investigation_completed"
            )

            self.trace.record(
                step="investigation",
                status=state.value,
            )

        except Exception as exc:
            state = WorkflowState.FAILED

            context.add_timeline_event(
                "investigation_failed",
                details={"error": str(exc)},
            )

            self.trace.record(
                step="investigation",
                status=state.value,
                details={"error": str(exc)},
            )

            raise

        return {
            "case_id": case_id,
            "state": state.value,
            "investigation": context.snapshot(),
            "trace": self.trace.all(),
        }

    @staticmethod
    def _state_for_step(step_name: str) -> WorkflowState:
        mapping = {
            "analysis": WorkflowState.ANALYZING,
            "enrichment": WorkflowState.ENRICHING,
            "decision": WorkflowState.DECIDING,
            "response": WorkflowState.RESPONDING,
        }

        return mapping.get(
            step_name,
            WorkflowState.ANALYZING,
        )

    @staticmethod
    def _apply_result(
        context: InvestigationContext,
        step_name: str,
        result: dict[str, Any],
    ) -> None:
        """
        Store step output in the appropriate context area.

        The orchestrator intentionally does not interpret domain
        semantics beyond routing the result into shared state.
        """

        if step_name == "analysis":
            context.evidence.append(result)

        elif step_name == "enrichment":
            context.threat_intelligence = dict(result)

        elif step_name == "decision":
            context.decisions.append(result)

        elif step_name == "response":
            context.response = dict(result)