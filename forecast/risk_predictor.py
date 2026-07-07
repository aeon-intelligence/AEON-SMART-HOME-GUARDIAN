"""
AEON MATRIX Inventory Risk Predictor
"""


def predict_inventory_risk(stock, forecast):

    if stock < forecast["forecast"]:
        risk = "HIGH"
        score = 85

    else:
        risk = "LOW"
        score = 20

    return {
        "risk_level": risk,
        "risk_score": score
    }
