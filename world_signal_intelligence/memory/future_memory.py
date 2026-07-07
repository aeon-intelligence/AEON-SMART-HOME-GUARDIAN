from datetime import datetime


def save(signal):

    return {
        "memory_type":
            "FUTURE_PREPAREDNESS_MEMORY",
        "signal": signal,
        "timestamp":
            datetime.utcnow().isoformat()
    }
