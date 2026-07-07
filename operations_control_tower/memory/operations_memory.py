from datetime import datetime


def save(record):

    return {
        "memory_type":
            "OPERATIONS_CONTROL_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
