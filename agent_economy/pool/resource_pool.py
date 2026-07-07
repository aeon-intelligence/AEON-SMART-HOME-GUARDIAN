class AgentResourcePool:

    def __init__(self):
        self.agents = []

    def register(self, name, capability, capacity):

        agent = {
            "name": name,
            "capability": capability,
            "capacity": capacity
        }

        self.agents.append(agent)

        return agent
