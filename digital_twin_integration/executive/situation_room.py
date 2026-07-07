from datetime import datetime


def create_snapshot(state):

    return {

        "system":
            "AEON MATRIX EXECUTIVE SITUATION ROOM",

        "inventory_health":
            state.inventory_health,

        "operational_risk":
            state.operational_risk,

        "timestamp":
            datetime.utcnow().isoformat()
    }
