"""
Intelligence Graph

Foundation for Sentinel DNA
knowledge relationships.
"""


class IntelligenceGraph:


    def __init__(self):

        self.nodes = []

        self.relationships = []



    def add_node(
        self,
        node_type,
        value
    ):

        node = {

            "type": node_type,

            "value": value

        }


        self.nodes.append(node)


        return node



    def connect(
        self,
        source,
        target,
        relation
    ):

        edge = {

            "source": source,

            "target": target,

            "relation": relation

        }


        self.relationships.append(edge)


        return edge