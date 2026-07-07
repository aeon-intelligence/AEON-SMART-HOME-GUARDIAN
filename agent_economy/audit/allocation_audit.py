from datetime import datetime


def log_allocation(record):

    return {
        "audit_event": record,
        "logged_at":
            datetime.utcnow().isoformat()
    }
