"""
AEON MATRIX Autonomous Optimization Engine
"""


def optimize_inventory(stock, demand):

    if stock < demand:
        action = "TRANSFER_STOCK"
        efficiency = 85

    else:
        action = "BALANCE_INVENTORY"
        efficiency = 95

    return {
        "optimization_action": action,
        "efficiency_score": efficiency
    }
