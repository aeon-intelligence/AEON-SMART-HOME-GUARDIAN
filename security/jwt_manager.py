"""
AEON MATRIX JWT Manager
Authentication Layer
"""

from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(subject: str, role: str):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "role": role,
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "valid": True,
            "payload": payload
        }

    except jwt.ExpiredSignatureError:
        return {
            "valid": False,
            "reason": "TOKEN_EXPIRED"
        }

    except jwt.InvalidTokenError:
        return {
            "valid": False,
            "reason": "INVALID_TOKEN"
        }
