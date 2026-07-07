"""
AEON MATRIX Threat Detection Engine
"""

def analyze_signal(signal):

    risk = 0

    if signal.get("token_failure", 0) > 5:
        risk += 40

    if signal.get("unknown_device"):
        risk += 40

    if signal.get("permission_violation"):
        risk += 30

    if risk >= 70:
        return {
            "status": "THREAT_DETECTED",
            "risk_score": risk,
            "action": "BLOCK_AND_REVIEW"
        }

    return {
        "status": "NORMAL",
        "risk_score": risk,
        "action": "ALLOW"
    }
