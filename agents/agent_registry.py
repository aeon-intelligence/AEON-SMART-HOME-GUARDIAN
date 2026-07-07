"""
AEON MATRIX Multi-Agent Registry
"""

AGENTS = {}


def register_agent(name, capability):

    AGENTS[name] = {
        "capability": capability,
        "status": "ONLINE"
    }

    return AGENTS[name]


def list_agents():

    return AGENTS
