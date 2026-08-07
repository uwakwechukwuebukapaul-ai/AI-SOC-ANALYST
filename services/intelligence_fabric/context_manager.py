"""
Investigation Context Manager

Maintains shared investigation memory.
"""


class InvestigationContextManager:


    def __init__(self):

        self.contexts = {}



    def create_context(
        self,
        case_id
    ):

        context = {

            "case_id": case_id,

            "alerts": [],

            "evidence": [],

            "iocs": [],

            "entities": [],

            "risk": None

        }


        self.contexts[case_id] = context


        return context



    def update(
        self,
        case_id,
        key,
        value
    ):

        context = self.contexts.get(
            case_id
        )


        if context:

            context[key].append(value)


        return context



    def get(
        self,
        case_id
    ):

        return self.contexts.get(
            case_id
        )