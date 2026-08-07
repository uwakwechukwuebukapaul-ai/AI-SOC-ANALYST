"""
Unified Investigation Runtime.

Coordinates the Sentinel DNA intelligence services through a stable,
dependency-injected investigation pipeline.
"""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from .decision_gate import DecisionGate
from .investigation_pipeline import (
    InvestigationPipeline,
    InvestigationStage,
)
from .runtime_result import InvestigationRuntimeResult
from .service_registry import ServiceRegistry


class InvestigationRuntime:
    """
    Main execution boundary for unified investigations.
    """

    def __init__(
        self,
        *,
        registry: ServiceRegistry | None = None,
        pipeline: InvestigationPipeline | None = None,
        decision_gate: DecisionGate | None = None,
    ) -> None:
        self.registry = registry or ServiceRegistry()
        self.pipeline = pipeline or InvestigationPipeline()
        self.decision_gate = decision_gate or DecisionGate()

    def register_service(
        self,
        name: str,
        service: Any,
        *,
        replace: bool = False,
    ) -> None:
        self.registry.register(
            name,
            service,
            replace=replace,
        )

    def register_stage(
        self,
        stage: InvestigationStage,
        handler,
        *,
        required: bool = False,
        replace: bool = False,
    ) -> None:
        self.pipeline.register(
            stage,
            handler,
            required=required,
            replace=replace,
        )

    def investigate(
        self,
        evidence: dict[str, Any] | None = None,
        *,
        investigation_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> InvestigationRuntimeResult:
        investigation_id = (
            investigation_id
            or f"INV-{uuid4().hex[:12].upper()}"
        )

        context: dict[str, Any] = {
            "investigation_id": investigation_id,
            "evidence": evidence or {},
            "metadata": metadata or {},
            "stages": {},
        }

        result = InvestigationRuntimeResult(
            investigation_id=investigation_id,
            metadata=metadata or {},
        )

        stage_results = self.pipeline.execute(context)

        for stage_result in stage_results:
            result.add_stage(stage_result)

        decision = self.decision_gate.evaluate(context)

        result.decision = decision.value

        result.status = (
            "failed"
            if any(stage.error for stage in stage_results)
            else "completed"
        )

        result.summary = self._build_summary(
            result,
            context,
        )

        result.metadata.update(
            {
                "registered_services": self.registry.names(),
                "executed_stages": [
                    stage.stage
                    for stage in stage_results
                ],
            }
        )

        result.complete()

        return result

    @staticmethod
    def _build_summary(
        result: InvestigationRuntimeResult,
        context: dict[str, Any],
    ) -> str:
        if result.failed_stages:
            failed = ", ".join(
                stage.stage
                for stage in result.failed_stages
            )

            return (
                "Investigation completed with stage failures: "
                f"{failed}."
            )

        return (
            "Unified investigation completed successfully "
            f"with decision '{result.decision}'."
        )