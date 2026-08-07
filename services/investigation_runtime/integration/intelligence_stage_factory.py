"""
Factory for creating Investigation Runtime stages backed by
registered intelligence services.
"""

from __future__ import annotations

from typing import Any, Callable

from ..investigation_pipeline import InvestigationStage, PipelineStep
from .runtime_service_registry import RuntimeServiceRegistry


class IntelligenceStageFactory:
    """
    Creates pipeline stages that delegate execution to
    registered intelligence services.
    """

    def __init__(
        self,
        registry: RuntimeServiceRegistry,
    ) -> None:
        if not isinstance(registry, RuntimeServiceRegistry):
            raise TypeError(
                "registry must be a RuntimeServiceRegistry."
            )

        self.registry = registry

    def create_handler(
        self,
        service_name: str,
    ) -> Callable[[dict[str, Any]], dict[str, Any]]:
        """
        Create a pipeline handler for a registered service.
        """

        if not self.registry.has(service_name):
            raise KeyError(
                f"Cannot create stage for unregistered "
                f"service '{service_name}'."
            )

        def handler(
            context: dict[str, Any],
        ) -> dict[str, Any]:
            return self.registry.execute(
                service_name,
                context,
            )

        return handler

    def create_step(
        self,
        stage: InvestigationStage,
        service_name: str,
        *,
        required: bool = False,
    ) -> PipelineStep:
        """
        Create a PipelineStep backed by a registered service.
        """

        if not isinstance(stage, InvestigationStage):
            raise TypeError(
                "stage must be an InvestigationStage."
            )

        return PipelineStep(
            stage=stage,
            handler=self.create_handler(service_name),
            required=required,
        )