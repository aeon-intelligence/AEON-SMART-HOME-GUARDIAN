from datetime import datetime


def add_decision(event):

    return {
        "event": event,
        "recorded_at":
            datetime.utcnow().isoformat()
    }
