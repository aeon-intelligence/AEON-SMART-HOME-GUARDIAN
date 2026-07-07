from datetime import datetime

def save(record):

    return {
        "memory_type": "DIGITAL_TWIN_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
