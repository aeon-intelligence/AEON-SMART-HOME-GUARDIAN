from datetime import datetime


def save(record):

    return {
        "memory_type": "DECISION_INTELLIGENCE_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
