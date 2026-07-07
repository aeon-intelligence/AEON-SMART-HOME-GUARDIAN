from datetime import datetime


def record(event):

    return {
        "audit_event": event,
        "timestamp":
            datetime.utcnow().isoformat()
    }
