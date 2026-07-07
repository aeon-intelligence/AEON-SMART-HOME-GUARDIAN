from datetime import datetime


def save(record):

    return {
        "memory_type":
            "WORLD_SIGNAL_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
