"""
Sentinel DNA Runtime Pipeline

Pipeline execution framework for intelligence workflows.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class PipelineStage:
    """
    Individual pipeline execution stage.
    """

    name: str

    handler: Callable

    enabled: bool = True


    def execute(
        self,
        data: Any,
    ) -> Any:
        """
        Execute stage.
        """

        if not self.enabled:
            return data

        return self.handler(data)



@dataclass
class RuntimePipeline:
    """
    Runtime execution pipeline.
    """

    name: str

    stages: list[PipelineStage] = field(
        default_factory=list
    )


    def add_stage(
        self,
        stage: PipelineStage,
    ) -> None:
        """
        Add execution stage.
        """

        self.stages.append(stage)



    def execute(
        self,
        data: Any,
    ) -> Any:
        """
        Execute pipeline stages.
        """

        result = data


        for stage in self.stages:

            result = stage.execute(
                result
            )


        return result



    def clear(self):

        self.stages.clear()



    def to_dict(self):

        return {
            "name": self.name,
            "stages": [
                {
                    "name": stage.name,
                    "enabled": stage.enabled,
                }
                for stage in self.stages
            ],
        }



class RuntimePipelineManager:
    """
    Pipeline registry.
    """

    def __init__(self):

        self.pipelines: dict[
            str,
            RuntimePipeline
        ] = {}



    def register(
        self,
        pipeline: RuntimePipeline,
    ):

        self.pipelines[pipeline.name] = pipeline



    def remove(
        self,
        name: str,
    ):

        self.pipelines.pop(
            name,
            None,
        )



    def execute(
        self,
        name: str,
        data: Any,
    ):

        pipeline = self.pipelines.get(name)


        if not pipeline:
            return None


        return pipeline.execute(
            data
        )



    def clear(self):

        self.pipelines.clear()



    def to_dict(self):

        return {
            "pipelines": [
                pipeline.to_dict()
                for pipeline in self.pipelines.values()
            ]
        }