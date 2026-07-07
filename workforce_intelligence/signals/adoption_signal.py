from datetime import datetime


def create_adoption_signal(score):

    return {
        "signal": "AI_ADOPTION_STATUS",
        "adoption_score": score,
        "timestamp": datetime.utcnow().isoformat()
    }
