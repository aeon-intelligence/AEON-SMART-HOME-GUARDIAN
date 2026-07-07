from datetime import datetime


def save(record):

    return {
        "memory_type":
            "EXECUTIVE_OPERATING_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
