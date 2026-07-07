from datetime import datetime


def save(record):

    return {
        "memory_type":
            "OPTIMIZATION_LEARNING_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
