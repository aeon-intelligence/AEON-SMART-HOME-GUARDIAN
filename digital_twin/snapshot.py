"""
AEON MATRIX Digital Twin Snapshot
"""


def snapshot(result):

    return {
        "twin_status": "ACTIVE",
        "simulation_status": result["simulation"],
        "action": result["recommended_action"]
    }
