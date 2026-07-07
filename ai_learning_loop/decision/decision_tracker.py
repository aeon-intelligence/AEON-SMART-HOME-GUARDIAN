from datetime import datetime


def record_decision(name, action):

    return {
        "decision": name,
        "action": action,
        "timestamp":
            datetime.utcnow().isoformat()
    }
