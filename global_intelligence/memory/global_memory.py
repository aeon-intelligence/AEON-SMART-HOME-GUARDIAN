from datetime import datetime


def save(record):

    return {
        "memory_type":
            "GLOBAL_INTELLIGENCE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
