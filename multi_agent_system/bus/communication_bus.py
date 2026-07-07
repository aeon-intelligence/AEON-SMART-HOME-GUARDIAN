class AgentBus:

    def publish(self, sender, message):

        return {
            "sender": sender,
            "message": message,
            "channel": "AGENT_BUS"
        }
