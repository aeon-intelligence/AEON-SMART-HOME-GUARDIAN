from datetime import datetime


def save(record):

    return {
        "memory_type": "ALERT_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
