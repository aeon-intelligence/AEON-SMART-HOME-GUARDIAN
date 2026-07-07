"""
AEON MATRIX Simulation Engine
"""


def simulate(twin):

    stock = twin.get("stock", 0)
    demand = twin.get("demand", 0)

    risk = "HIGH" if demand > stock else "LOW"

    return {
        "simulation": "COMPLETED",
        "inventory_risk": risk,
        "recommended_action":
            "TRANSFER_STOCK"
            if risk == "HIGH"
            else "NORMAL_OPERATION"
    }
