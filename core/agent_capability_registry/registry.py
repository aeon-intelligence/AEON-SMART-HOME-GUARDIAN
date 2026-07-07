"""
AEON MATRIX Enterprise Agent Capability Registry

Manage AI agent capabilities, health and performance.
"""


class AgentCapabilityRegistry:

    def __init__(self):

        self.registry = {}

    def register(
        self,
        agent_id,
        capability
    ):

        self.registry[agent_id] = {
            "capability": capability,
            "health_score": 100,
            "performance_score": 0,
            "status": "ACTIVE"
        }

    def update_performance(
        self,
        agent_id,
        score
    ):

        if agent_id in self.registry:

            self.registry[agent_id][
                "performance_score"
            ] = score

    def get_agent(
        self,
        agent_id
    ):

        return self.registry.get(
            agent_id,
            None
        )
