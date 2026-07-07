from datetime import datetime


def create_signal(system):

    return {
        "signal":
            "PREDICTIVE_MAINTENANCE",
        "system": system,
        "timestamp":
            datetime.utcnow().isoformat()
    }
