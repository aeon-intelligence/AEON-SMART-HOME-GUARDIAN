from datetime import datetime


def save(record):

    return {
        "memory_type":
            "DIGITAL_TWIN_SIMULATION_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
