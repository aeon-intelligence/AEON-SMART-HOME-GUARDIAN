from datetime import datetime


def generate_dashboard(signal):

    return {
        "dashboard": "AEON MATRIX EXECUTIVE COMMAND CENTER",
        "system_health": 100,
        "priority": signal.get("priority"),
        "risk_score": signal.get("risk_score"),
        "business_area": signal.get(
            "business_impact",
            {}
        ).get("operation"),
        "generated_at": datetime.utcnow().isoformat()
    }
