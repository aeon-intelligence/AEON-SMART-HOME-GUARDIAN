from datetime import datetime


def record(event):

    return {
        "event": event,
        "timestamp":
            datetime.utcnow().isoformat()
    }
