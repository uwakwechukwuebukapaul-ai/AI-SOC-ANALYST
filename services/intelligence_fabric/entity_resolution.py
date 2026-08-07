"""
Entity Resolution Engine

Links security entities together.
"""


class EntityResolver:


    def __init__(self):

        self.entities = []


    def resolve(self, entity):

        record = {
            "type": entity.get(
                "type",
                "unknown"
            ),
            "value": entity.get(
                "value"
            ),
            "relationships": []
        }


        self.entities.append(record)

        return record


    def link(
        self,
        source,
        target,
        relationship
    ):

        relation = {

            "source": source,

            "target": target,

            "relationship": relationship

        }


        return relation