from datetime import datetime


def create_token(user):

    return {
        "user": user,
        "token_status": "VALID",
        "issued_at": datetime.utcnow().isoformat()
    }
