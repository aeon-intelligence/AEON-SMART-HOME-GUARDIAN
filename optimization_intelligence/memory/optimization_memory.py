from datetime import datetime


def save(record):

    return {
        "memory_type": "OPTIMIZATION_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
