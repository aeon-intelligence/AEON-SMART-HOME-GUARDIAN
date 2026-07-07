from datetime import datetime


def save(record):

    return {
        "memory_type":
            "INNOVATION_LEARNING",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
