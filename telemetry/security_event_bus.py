"""
AEON MATRIX Security Event Bus
"""

from datetime import datetime
import uuid


def create_security_event(
    event_type,
    source,
    risk_score,
    action
):

    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "source": source,
        "risk_score": risk_score,
        "action": action
    }
