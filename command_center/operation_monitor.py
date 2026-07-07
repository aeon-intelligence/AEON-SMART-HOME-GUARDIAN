"""
AEON MATRIX Operation Monitor
"""


def analyze_operation(events):

    risk = 0

    for event in events:

        payload = event.get("payload", {})

        if payload.get("stock_risk",0) > 70:
            risk += 30

        if payload.get("delay_risk",0) > 70:
            risk += 30

        if payload.get("route_risk",0) > 70:
            risk += 20

    return {
        "risk_score": risk,
        "status":
            "CRITICAL" if risk >=70
            else "NORMAL"
    }
