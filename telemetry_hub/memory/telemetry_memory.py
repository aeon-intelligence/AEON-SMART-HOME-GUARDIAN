from datetime import datetime


def save(record):

    return {
        "memory_type":
            "REAL_TIME_TELEMETRY_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
