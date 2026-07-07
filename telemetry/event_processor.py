"""
AEON MATRIX Event Processor
"""


def process(event):

    risk = event.get("risk_score", 0)

    if risk >= 80:
        decision = "ESCALATE_TO_GUARDIAN"
    else:
        decision = "NORMAL_MONITORING"

    return {
        "event": event["event_type"],
        "decision": decision
    }
