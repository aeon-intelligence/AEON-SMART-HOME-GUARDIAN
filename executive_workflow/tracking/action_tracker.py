from datetime import datetime


def track(action):

    return {
        "action": action,
        "status": "MONITORING",
        "timestamp":
            datetime.utcnow().isoformat()
    }
