"""
AEON MATRIX Agent Status Registry
"""

AGENTS = []


def register_agent(name, role, status):

    agent = {
        "name": name,
        "role": role,
        "status": status
    }

    AGENTS.append(agent)

    return agent


def get_agents():

    return AGENTS
