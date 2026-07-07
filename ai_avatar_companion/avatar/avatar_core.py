from datetime import datetime


def create_avatar(name, role):

    return {
        "avatar": name,
        "role": role,
        "status": "ACTIVE",
        "created_at":
            datetime.utcnow().isoformat()
    }
