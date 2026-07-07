"""
AEON MATRIX Simulation Engine
"""


def simulate_operation(twin):

    state = twin.get("state", {})

    risk = 0

    if state.get("inventory_shortage"):
        risk += 40

    if state.get("delay_risk"):
        risk += 30

    if state.get("capacity_pressure"):
        risk += 20

    if risk >= 70:
        decision = "OPTIMIZE_AND_ESCALATE"

    elif risk >= 40:
        decision = "MONITOR_AND_ADJUST"

    else:
        decision = "CONTINUE_OPERATION"

    return {
        "simulation_status": "COMPLETED",
        "risk_score": risk,
        "recommended_action": decision
    }
