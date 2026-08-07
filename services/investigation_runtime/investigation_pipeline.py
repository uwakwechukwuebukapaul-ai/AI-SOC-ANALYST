"""
Investigation pipeline.

Provides deterministic stage registration and execution while keeping
individual intelligence services decoupled from the runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable

from .runtime_result import StageResult


class InvestigationStage(str, Enum):
    RISK = "risk"
    MITRE = "mitre"
    DETECTION = "detection"
    THREAT_HUNT = "threat_hunt"
    DECISION = "decision"
    COPILOT = "copilot"
    SOAR = "soar"


StageHandler = Callable[[dict[str, Any]], dict[str, Any]]


@dataclass
class PipelineStep:
    stage: InvestigationStage
    handler: StageHandler
    required: bool = False


class InvestigationPipeline:
    """
    Executes registered investigation stages in order.
    """

    DEFAULT_ORDER = (
        InvestigationStage.RISK,
        InvestigationStage.MITRE,
        InvestigationStage.DETECTION,
        InvestigationStage.THREAT_HUNT,
        InvestigationStage.DECISION,
        InvestigationStage.COPILOT,
        InvestigationStage.SOAR,
    )

    def __init__(self) -> None:
        self._steps: dict[InvestigationStage, PipelineStep] = {}

    def register(
        self,
        stage: InvestigationStage,
        handler: StageHandler,
        *,
        required: bool = False,
        replace: bool = False,
    ) -> None:
        if stage in self._steps and not replace:
            raise ValueError(
                f"Pipeline stage already registered: {stage.value}"
            )

        if not callable(handler):
            raise TypeError("Pipeline handler must be callable.")

        self._steps[stage] = PipelineStep(
            stage=stage,
            handler=handler,
            required=required,
        )

    def unregister(
        self,
        stage: InvestigationStage,
    ) -> PipelineStep | None:
        return self._steps.pop(stage, None)

    def stages(self) -> list[InvestigationStage]:
        return [
            stage
            for stage in self.DEFAULT_ORDER
            if stage in self._steps
        ]

    def execute(
        self,
        context: dict[str, Any],
    ) -> list[StageResult]:
        results: list[StageResult] = {}

        output: list[StageResult] = []

        for stage in self.stages():
            step = self._steps[stage]

            result = StageResult(stage=stage.value)

            try:
                stage_data = step.handler(context)

                if stage_data is None:
                    stage_data = {}

                if not isinstance(stage_data, dict):
                    stage_data = {
                        "result": stage_data,
                    }

                result.data = stage_data
                result.status = "completed"

                context.setdefault("stages", {})[
                    stage.value
                ] = stage_data

            except Exception as exc:
                result.status = "failed"
                result.error = str(exc)

                if step.required:
                    result.complete()
                    output.append(result)
                    break

            result.complete()
            output.append(result)

        return output