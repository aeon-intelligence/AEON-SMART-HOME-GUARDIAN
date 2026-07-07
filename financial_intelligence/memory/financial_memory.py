from datetime import datetime


def save(record):

    return {
        "memory_type":
            "FINANCIAL_INTELLIGENCE_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
