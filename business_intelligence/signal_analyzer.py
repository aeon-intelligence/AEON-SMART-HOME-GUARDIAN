"""
AEON MATRIX Business Signal Analyzer
"""


def evaluate(kpi):

    if kpi["risk_level"] == "LOW":
        decision = "OPTIMIZE_GROWTH"
    else:
        decision = "ESCALATE"

    return {
        "decision": decision,
        "confidence": 92
    }
