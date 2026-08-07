"""
Sentinel DNA Runtime Execution Result

Enterprise execution result contract.

Responsibilities:

- standardize runtime responses
- support dictionary compatibility
- expose execution metadata
- support workflow consumers
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionResult:
    """
    Runtime execution response object.
    """

    success: bool = False

    output: Any = None

    error: str | None = None

    confidence: float | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    @classmethod
    def ok(
        cls,
        data: Any = None,
        output: Any = None,
        confidence: float | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ExecutionResult":
        """
        Create successful execution result.
        """

        if output is None:
            output = data


        return cls(
            success=True,
            output=output,
            confidence=confidence,
            metadata=metadata or {},
        )


    @classmethod
    def failure(
        cls,
        error: str,
        confidence: float | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ExecutionResult":
        """
        Create failed execution result.
        """

        return cls(
            success=False,
            error=error,
            confidence=confidence,
            metadata=metadata or {},
        )


    @property
    def failed(self) -> bool:
        """
        Check execution failure.
        """

        return not self.success


    @property
    def data(self):
        """
        Compatibility alias.
        """

        return self.output


    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Add execution metadata.
        """

        self.metadata[key] = value



    def to_dict(self) -> dict[str, Any]:
        """
        Convert result to dictionary.
        """

        return {
            "success": self.success,
            "output": self.output,
            "error": self.error,
            "confidence": self.confidence,
            "metadata": self.metadata,
        }



    def __getitem__(
        self,
        key: str,
    ):
        """
        Dictionary compatibility access.

        Supports:

        result["done"]

        when output:

        {
            "done": True
        }

        or:

        {
            "result": {
                "done": True
            }
        }
        """

        if isinstance(
            self.output,
            dict,
        ):

            if key in self.output:
                return self.output[key]


            nested = self.output.get(
                "result"
            )


            if isinstance(
                nested,
                dict,
            ):

                return nested[key]


        return self.to_dict()[key]



    def get(
        self,
        key: str,
        default=None,
    ):
        """
        Dictionary-style get support.
        """

        try:
            return self[key]

        except KeyError:
            return default



    def __contains__(
        self,
        key: str,
    ) -> bool:
        """
        Support:

        key in result
        """

        try:

            self[key]

            return True

        except KeyError:

            return False



    def __bool__(self):
        """
        Truth evaluation.
        """

        return self.success