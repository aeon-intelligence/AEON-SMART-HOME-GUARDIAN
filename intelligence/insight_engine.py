"""
AEON MATRIX Operational Insight Engine
"""


def generate_insight(signal):

    if signal["status"] == "CRITICAL":
        action = "ESCALATE_TO_GUARDIAN"

    elif signal["status"] == "WARNING":
        action = "MONITOR"

    else:
        action = "CONTINUE_OPERATION"

    return {
        "decision": action,
        "signal_status": signal["status"],
        "risk_score": signal["risk_score"]
    }
