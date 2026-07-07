from datetime import datetime


def create_state(system, metrics):

    return {
        "system": system,
        "metrics": metrics,
        "timestamp":
            datetime.utcnow().isoformat()
    }
