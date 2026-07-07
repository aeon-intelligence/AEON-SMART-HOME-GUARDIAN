from datetime import datetime


def save(record):

    return {
        "memory_type":
            "HUMAN_AI_COLLABORATION_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
