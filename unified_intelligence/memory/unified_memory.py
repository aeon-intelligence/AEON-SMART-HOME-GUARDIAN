from datetime import datetime


def save(record):

    return {
        "memory_type":
            "UNIFIED_ENTERPRISE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
