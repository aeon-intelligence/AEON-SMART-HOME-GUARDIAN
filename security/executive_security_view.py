"""
AEON MATRIX Executive Security View
"""


def generate_security_summary(events):

    high_risk = [
        e for e in events
        if e.get("risk_score",0) >= 70
    ]

    return {
        "total_events": len(events),
        "high_risk_events": len(high_risk),
        "security_status":
            "ATTENTION_REQUIRED"
            if high_risk
            else "NORMAL"
    }
