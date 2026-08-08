"""
Sentinel DNA Attack Story Builder

Creates a human-readable attack narrative.
"""

from __future__ import annotations

from typing import Any



class AttackStoryBuilder:
    """
    Converts technical findings into
    investigation narrative.
    """

    def build(
        self,
        reasoning: dict[str, Any],
    ) -> str:
        """
        Build attack explanation.
        """

        hypotheses = reasoning.get(
            "hypotheses",
            [],
        )


        if not hypotheses:

            return (
                "No confirmed attack story "
                "could be generated."
            )


        statements = []


        for item in hypotheses:

            statements.append(
                item.get(
                    "hypothesis",
                    "Unknown activity",
                )
            )


        return (
            "Investigation analysis indicates: "
            +
            " ".join(statements)
        )