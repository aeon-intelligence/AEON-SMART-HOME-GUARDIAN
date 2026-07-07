from datetime import datetime

def log(event):

    return {
        "event": event,
        "timestamp": datetime.utcnow().isoformat()
    }
