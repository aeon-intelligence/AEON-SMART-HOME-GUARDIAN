class AgentRegistry:

    def __init__(self):
        self.agents = {}

    def register(self, name, role):

        self.agents[name] = {
            "role": role,
            "status": "ACTIVE"
        }

        return self.agents[name]
