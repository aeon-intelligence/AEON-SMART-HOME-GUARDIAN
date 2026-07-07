"""
AEON MATRIX Forecast Intelligence Snapshot
"""


def snapshot(forecast, risk, scenario):

    return {
        "forecast_confidence": forecast["confidence"],
        "risk": risk["risk_level"],
        "future_action": scenario["recommended_action"]
    }
