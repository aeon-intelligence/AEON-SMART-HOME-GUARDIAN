from datetime import datetime


def save(record):

    return {
        "memory_type":
            "BUSINESS_VALUE_MEMORY",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
