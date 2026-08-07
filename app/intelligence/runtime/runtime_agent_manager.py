"""
Runtime Agent Manager

Responsible for managing AI agents
inside Sentinel DNA runtime layer.
"""


class RuntimeAgentManager:

    def __init__(self):

        self.agents = {}


    def register(self, agent):

        name = getattr(
            agent,
            "name",
            None
        )

        if name is None:

            metadata = getattr(
                agent,
                "metadata",
                None
            )

            name = getattr(
                metadata,
                "name",
                None
            )


        if name is None:
            raise ValueError(
                "Agent must have a name"
            )


        self.agents[name] = agent

        return agent



    def get(self, name):

        return self.agents.get(name)



    def unregister(self, name):

        return self.agents.pop(
            name,
            None
        )



    def clear(self):

        self.agents.clear()



    def count(self):

        return len(
            self.agents
        )



    def list_agents(self):

        return list(
            self.agents.keys()
        )



    def status(self):

        return {

            "agents": self.list_agents(),

            "count": self.count()

        }