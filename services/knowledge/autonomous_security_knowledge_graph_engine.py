"""
Autonomous Security Knowledge Graph Engine

Sentinel DNA Intelligence Graph Layer

Responsibilities:
- create security entities
- build entity relationships
- discover threat connections
- map attack paths
- analyze threat clusters
- maintain graph intelligence history
"""

from datetime import datetime, timezone
import uuid


class AutonomousSecurityKnowledgeGraphEngine:

    def __init__(self):
        self.entities = {}
        self.relationships = []
        self.history = []

    def create_entity(self, entity_type, name, metadata=None):

        entity_id = f"ENT-{uuid.uuid4().hex[:8].upper()}"

        entity = {
            "id": entity_id,
            "type": entity_type,
            "name": name,
            "metadata": metadata or {},
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.entities[entity_id] = entity
        self.history.append(entity)

        return entity

    def create_relationship(
        self,
        source_id,
        target_id,
        relationship_type
    ):

        relationship = {
            "source": source_id,
            "target": target_id,
            "type": relationship_type,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.relationships.append(relationship)
        self.history.append(relationship)

        return relationship

    def find_related_entities(self, entity_id):

        related = []

        for relation in self.relationships:

            if relation["source"] == entity_id:
                related.append(
                    self.entities.get(
                        relation["target"]
                    )
                )

            elif relation["target"] == entity_id:
                related.append(
                    self.entities.get(
                        relation["source"]
                    )
                )

        return [
            item for item in related
            if item
        ]

    def map_attack_path(self, start_entity):

        path = []

        current = start_entity

        visited = set()

        while current and current not in visited:

            visited.add(current)

            entity = self.entities.get(
                current
            )

            if not entity:
                break

            path.append(entity)

            next_entities = self.find_related_entities(
                current
            )

            if not next_entities:
                break

            current = next_entities[0]["id"]

        return path

    def analyze_threat_cluster(self, entity_id):

        connections = self.find_related_entities(
            entity_id
        )

        return {
            "entity": entity_id,
            "cluster_size": len(connections),
            "risk_level":
                "high"
                if len(connections) >= 3
                else "medium"
        }

    def get_history(self):

        return self.history