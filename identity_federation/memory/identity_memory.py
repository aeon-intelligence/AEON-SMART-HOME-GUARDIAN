from datetime import datetime

def save(record):
    return {
        "memory_type": "IDENTITY_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
