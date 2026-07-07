from datetime import datetime


def save(record):

    return {
        "memory_type":
            "FUTURE_SIGNAL_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
