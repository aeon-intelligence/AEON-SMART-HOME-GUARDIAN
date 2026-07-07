from datetime import datetime


def save(record):

    return {
        "memory_type":
            "ENTERPRISE_RISK_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
