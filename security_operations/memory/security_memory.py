from datetime import datetime

def save(record):
    return {
        "memory_type": "SECURITY_INCIDENT_MEMORY",
        "record": record,
        "timestamp": datetime.utcnow().isoformat()
    }
