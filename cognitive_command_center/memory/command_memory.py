from datetime import datetime


def save(record):

    return {
        "type":
            "COMMAND_CENTER_MEMORY",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
