from datetime import datetime


def save(record):

    return {
        "memory_type":
            "EXECUTIVE_DECISION_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
