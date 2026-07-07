from datetime import datetime


def save(record):

    return {
        "memory_type":
            "DIGITAL_TWIN_LIVE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
