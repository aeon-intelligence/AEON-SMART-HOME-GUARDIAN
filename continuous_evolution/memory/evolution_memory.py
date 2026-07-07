from datetime import datetime


def save(record):

    return {
        "memory_type":
            "CONTINUOUS_EVOLUTION_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
