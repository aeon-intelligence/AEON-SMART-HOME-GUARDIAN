"""
Enterprise Agent Capability Registry
"""


class AgentRegistry:

    def register(self, agent: dict):

        return {
            "agent_id": agent.get("id"),
            "capability": agent.get("capability"),
            "registered": True
        }
