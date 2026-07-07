from datetime import datetime

def log_event(event, actor):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "actor": actor
    }
