from datetime import datetime


def create_security_signal(event):

    return {
        "event": event,
        "severity": "HIGH",
        "timestamp":
            datetime.utcnow().isoformat()
    }
