"""
Sentinel DNA Runtime Execution Pipeline

Controls ordered execution stages inside
the Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class ExecutionPipeline:
    """
    Runtime execution pipeline manager.
    """

    stages: list[Callable] = field(
        default_factory=list
    )


    def add_stage(
        self,
        stage: Callable,
    ) -> None:
        """
        Add execution stage.
        """

        self.stages.append(stage)



    def remove_stage(
        self,
        stage: Callable,
    ) -> None:
        """
        Remove execution stage.
        """

        if stage in self.stages:
            self.stages.remove(stage)



    def clear(self) -> None:
        """
        Clear pipeline stages.
        """

        self.stages.clear()



    def execute(
        self,
        payload: Any,
    ) -> Any:
        """
        Execute payload through pipeline.
        """

        result = payload

        for stage in self.stages:
            result = stage(result)

        return result



    def size(self) -> int:
        """
        Pipeline stage count.
        """

        return len(self.stages)



    def status(self) -> dict:
        """
        Pipeline state.
        """

        return {
            "stages": self.size(),
        }