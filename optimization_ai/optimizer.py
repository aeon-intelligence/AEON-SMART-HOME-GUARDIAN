"""
AEON MATRIX Autonomous Business Optimization Engine
"""


def optimize(kpi):

    if kpi.get("inventory_health", 0) < 90:
        action = "OPTIMIZE_INVENTORY"
    else:
        action = "ACCELERATE_GROWTH"

    return {
        "optimization_status": "ACTIVE",
        "recommended_action": action
    }
