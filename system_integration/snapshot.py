"""
AEON MATRIX Final Operational Snapshot
"""


def snapshot(core, health, loop):

    return {
        "system": "AEON MATRIX",
        "integration": core["integration_status"],
        "health": health["status"],
        "control_loop": loop["decision_flow"]
    }
