from datetime import datetime


def monitor_state(operation, health):

    return {
        "operation": operation,
        "health_score": health,
        "timestamp":
            datetime.utcnow().isoformat()
    }
