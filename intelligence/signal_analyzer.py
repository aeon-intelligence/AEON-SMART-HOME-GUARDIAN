"""
AEON MATRIX Signal Analyzer
"""


def analyze_signal(event):

    payload = event.get("payload", {})

    risk = 0

    if payload.get("inventory_risk", 0) > 70:
        risk += 30

    if payload.get("sla_risk", 0) > 70:
        risk += 30

    if payload.get("market_pressure", 0) > 70:
        risk += 20

    if risk >= 70:
        status = "CRITICAL"

    elif risk >= 30:
        status = "WARNING"

    else:
        status = "NORMAL"

    return {
        "status": status,
        "risk_score": risk
    }
