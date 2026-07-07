from datetime import datetime


def save(record):

    return {
        "memory_type":
            "SELF_EVOLUTION_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
