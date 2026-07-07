from datetime import datetime


def save(record):

    return {
        "memory_type":
            "WORKFORCE_INTELLIGENCE",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
