"""
AEON MATRIX Executive Control Tower Snapshot
"""


def create_snapshot(health, agents, decisions):

    return {
        "system_health": health,
        "active_agents": len(agents),
        "latest_decision": decisions[-1]
        if decisions else None,
        "tower_status": "ONLINE"
    }
