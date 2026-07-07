"""
AEON MATRIX Digital Twin Executive Snapshot
"""


def snapshot(state, simulation, optimization):

    return {
        "digital_twin": "LIVE",
        "simulation": simulation["simulation_status"],
        "optimization": optimization["optimization"]
    }
