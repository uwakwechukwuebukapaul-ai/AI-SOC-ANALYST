"""
Sentinel DNA Runtime Execution Manager

Enterprise execution control layer.

Responsibilities:

- manage runtime execution
- submit jobs
- execute pipeline
- track execution metrics
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_pipeline import RuntimePipeline


@dataclass
class RuntimeExecutionManager:
    """
    Runtime execution coordinator.
    """

    pipeline: RuntimePipeline = field(
        default_factory=RuntimePipeline
    )

    executions: int = 0


    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register execution capability.
        """

        self.pipeline.register_handler(
            capability,
            handler,
        )



    def submit(
        self,
        capability: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Submit execution request.
        """

        self.pipeline.submit(
            capability,
            payload,
        )



    def execute(self) -> Any:
        """
        Execute next runtime job.
        """

        result = self.pipeline.process()


        if result is not None:
            self.executions += 1


        return result



    def pending(
        self,
    ) -> int:
        """
        Pending execution count.
        """

        return self.pipeline.size()



    def clear(self) -> None:
        """
        Reset execution manager.
        """

        self.pipeline.clear()

        self.executions = 0



    def status(self) -> dict[str, Any]:
        """
        Runtime execution status.
        """

        return {
            "executions":
                self.executions,

            "pending":
                self.pending(),

            "pipeline":
                self.pipeline.status(),
        }