from datetime import datetime


def save(record):

    return {
        "memory_type":
            "ORGANIZATIONAL_KNOWLEDGE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
