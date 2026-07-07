from datetime import datetime


def create_learning_signal(score):

    return {
        "signal_type": "OUTCOME_LEARNING",
        "decision_quality_score": score,
        "timestamp": datetime.utcnow().isoformat()
    }
