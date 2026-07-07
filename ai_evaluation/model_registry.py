"""
AEON MATRIX AI Model Registry
"""

MODELS = [
    "demand_forecast_model",
    "risk_prediction_model",
    "optimization_model"
]


def registry():

    return {
        "models": len(MODELS),
        "status": "ACTIVE"
    }
