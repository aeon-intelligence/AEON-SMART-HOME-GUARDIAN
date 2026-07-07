from datetime import datetime


def record(decision):

    return {
        "decision": decision,
        "timestamp":
            datetime.utcnow().isoformat(),
        "audit_status": "RECORDED"
    }
