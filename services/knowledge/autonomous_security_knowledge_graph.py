from datetime import datetime, timezone


class AutonomousSecurityKnowledgeGraph:
    """
    Autonomous Security Knowledge Graph Engine

    Maintains security entities and relationships for
    AI-driven SOC investigations.
    """

    def __init__(self):
        self.entities = {}
        self.relationships = []
        self.history = []

    def add_entity(self, entity_id, entity_type, attributes=None):
        entity = {
            "id": entity_id,
            "type": entity_type,
            "attributes": attributes or {},
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.entities[entity_id] = entity

        self.history.append({
            "action": "entity_created",
            "entity": entity_id,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return entity

    def get_entity(self, entity_id):
        return self.entities.get(entity_id)

    def add_relationship(self, source, relation, target):
        relationship = {
            "source": source,
            "relation": relation,
            "target": target,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.relationships.append(relationship)

        self.history.append({
            "action": "relationship_created",
            "relationship": relationship,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return relationship

    def query_relationships(self, entity_id):
        results = []

        for relationship in self.relationships:
            if (
                relationship["source"] == entity_id
                or relationship["target"] == entity_id
            ):
                results.append(relationship)

        return results

    def find_attack_path(self, start_entity, target_entity):
        visited = set()
        queue = [[start_entity]]

        while queue:
            path = queue.pop(0)
            current = path[-1]

            if current == target_entity:
                return path

            if current in visited:
                continue

            visited.add(current)

            for relationship in self.relationships:
                if relationship["source"] == current:
                    queue.append(
                        path + [relationship["target"]]
                    )

        return None

    def learn_pattern(self, entity_type):
        matches = []

        for entity in self.entities.values():
            if entity["type"] == entity_type:
                matches.append(entity)

        return {
            "pattern_type": entity_type,
            "count": len(matches),
            "entities": matches
        }

    def get_history(self):
        return self.history

    def clear_graph(self):
        self.entities.clear()
        self.relationships.clear()
        self.history.clear()

        return True