"""
Sentinel DNA Evidence Graph

Maintains relationships between
investigation entities.
"""

from __future__ import annotations

from typing import Any


class EvidenceGraph:

    def __init__(self):

        self.nodes: dict[str, dict[str, Any]] = {}

        self.edges: list[dict[str, str]] = []


    def add_entity(
        self,
        entity_id: str,
        entity_type: str,
        data: dict[str, Any],
    ):

        self.nodes[entity_id] = {
            "type": entity_type,
            "data": data,
        }


    def add_relationship(
        self,
        source: str,
        target: str,
        relationship: str,
    ):

        self.edges.append(
            {
                "source": source,
                "target": target,
                "relationship": relationship,
            }
        )


    def get_graph(self):

        return {
            "nodes": self.nodes,
            "edges": self.edges,
        }