"""
AEON MATRIX Future Scenario Simulator
"""


def simulate(forecast, risk):

    if risk["risk_level"] == "HIGH":

        action = "INCREASE_STOCK_OR_TRANSFER"

    else:

        action = "NORMAL_OPERATION"

    return {
        "scenario": "SIMULATED",
        "recommended_action": action
    }
