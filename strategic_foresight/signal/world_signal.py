from datetime import datetime


def collect_signal(source, impact):

    return {
        "source": source,
        "impact": impact,
        "timestamp":
            datetime.utcnow().isoformat()
    }
