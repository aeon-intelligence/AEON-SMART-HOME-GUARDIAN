"""
AEON MATRIX Event Classification
"""


def classify(event):

    payload = event.get("payload", {})

    risk = 0

    if payload.get("risk",0) > 70:
        risk = "HIGH"

    else:
        risk = "NORMAL"

    return {
        "classification": risk,
        "event": event["event_type"]
    }
