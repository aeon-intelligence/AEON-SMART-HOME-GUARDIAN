from datetime import datetime


def save(record):

    return {
        "memory_type":
            "DIGITAL_TWIN_DECISION",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
