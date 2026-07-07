from datetime import datetime


def check_health(service, score):

    return {
        "service": service,
        "health_score": score,
        "timestamp":
            datetime.utcnow().isoformat()
    }
