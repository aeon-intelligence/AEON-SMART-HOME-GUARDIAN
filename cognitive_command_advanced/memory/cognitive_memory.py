from datetime import datetime


def save(record):

    return {
        "memory_type":
            "COGNITIVE_COMMAND_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
