class AgentMemory:

    def __init__(self):
        self.memory = []

    def store(self, agent, insight):

        record = {
            "agent": agent,
            "insight": insight
        }

        self.memory.append(record)

        return record
