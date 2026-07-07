from datetime import datetime


def save(record):

    return {
        "memory_type":
            "INNOVATION_LEARNING_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
