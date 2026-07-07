from datetime import datetime


def collect_signal(source, value):

    return {
        "source": source,
        "value": value,
        "timestamp":
            datetime.utcnow().isoformat()
    }
