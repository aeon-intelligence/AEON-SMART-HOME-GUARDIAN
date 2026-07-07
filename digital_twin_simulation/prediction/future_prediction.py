from datetime import datetime


def predict(risk):

    return {
        "future_state":
            "Potential operational impact"
            if risk["risk_score"] > 70
            else "Normal operation",

        "confidence": 0.85,

        "timestamp":
            datetime.utcnow().isoformat()
    }
