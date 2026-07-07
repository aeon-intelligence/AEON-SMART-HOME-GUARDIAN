"""
AEON MATRIX Demand Forecast Engine
"""


def forecast_demand(history):

    if not history:
        return {
            "forecast": 0,
            "confidence": 0
        }

    average = sum(history) / len(history)

    trend = (
        "GROWTH"
        if history[-1] > average
        else "DECLINE"
    )

    return {
        "forecast": round(average,2),
        "trend": trend,
        "confidence": 90
    }
