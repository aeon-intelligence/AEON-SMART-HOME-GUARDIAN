from datetime import datetime


def save(record):

    return {
        "memory_type": "EXECUTIVE_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
