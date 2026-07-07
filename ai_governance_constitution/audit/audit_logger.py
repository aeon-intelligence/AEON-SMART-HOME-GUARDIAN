from datetime import datetime


def record(event):

    return {
        "event": event,
        "audit_status":
            "RECORDED",
        "timestamp":
            datetime.utcnow().isoformat()
    }
