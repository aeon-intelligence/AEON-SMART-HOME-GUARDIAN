from datetime import datetime


def save(event):

    return {
        "memory_type": "INTEGRATION_MEMORY",
        "event": event,
        "timestamp": datetime.utcnow().isoformat()
    }
