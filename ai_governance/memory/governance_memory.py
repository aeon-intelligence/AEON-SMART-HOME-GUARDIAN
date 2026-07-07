from datetime import datetime


def save(record):

    return {
        "memory_type":
            "AI_GOVERNANCE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
