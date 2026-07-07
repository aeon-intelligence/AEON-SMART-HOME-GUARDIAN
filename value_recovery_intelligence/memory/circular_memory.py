from datetime import datetime


def save(record):

    return {
        "memory_type":
            "CIRCULAR_VALUE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
