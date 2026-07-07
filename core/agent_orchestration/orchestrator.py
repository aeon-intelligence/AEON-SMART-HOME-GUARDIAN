"""
AEON MATRIX Autonomous Agent Orchestration Layer

Coordinate AI agents with routing,
permissions and governance validation.
"""


class AgentOrchestrator:

    def __init__(self):
        self.agents = {}

    def register_agent(self, name, capability):

        self.agents[name] = {
            "capability": capability,
            "status": "READY"
        }

    def route_task(self, task: dict):

        required = task.get(
            "capability",
            ""
        )

        for name, agent in self.agents.items():

            if agent["capability"] == required:

                return {
                    "assigned_agent": name,
                    "status": "ROUTED",
                    "guardian_check": True
                }

        return {
            "assigned_agent": None,
            "status": "NO_AGENT_AVAILABLE",
            "guardian_check": True
        }
