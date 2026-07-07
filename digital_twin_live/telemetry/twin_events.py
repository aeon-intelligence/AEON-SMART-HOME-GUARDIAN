from datetime import datetime


def create_twin_event(event_type, payload):
    return {
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload
    }
