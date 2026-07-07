from datetime import datetime


def save(record):

    return {
        "memory_type":
            "MULTI_AGENT_LEARNING_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
