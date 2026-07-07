from datetime import datetime


def create_dashboard_feed(signal):

    return {
        "dashboard": "AEON EXECUTIVE COMMAND CENTER",
        "status": signal["priority"],
        "summary": "Executive signal generated",
        "timestamp": datetime.utcnow().isoformat()
    }
