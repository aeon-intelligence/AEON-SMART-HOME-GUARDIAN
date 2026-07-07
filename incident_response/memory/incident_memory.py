from datetime import datetime


def store(record):

    return {
        "stored": True,
        "incident_record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
