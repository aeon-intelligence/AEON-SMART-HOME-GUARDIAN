from datetime import datetime


def save(record):

    return {
        "memory_type": "WORKFLOW_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
