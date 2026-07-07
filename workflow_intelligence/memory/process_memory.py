from datetime import datetime


def save(record):

    return {
        "memory_type":
            "PROCESS_INTELLIGENCE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
