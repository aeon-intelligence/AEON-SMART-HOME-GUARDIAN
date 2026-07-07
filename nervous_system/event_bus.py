"""
AEON MATRIX Enterprise Event Bus
"""

from datetime import datetime
import uuid

EVENT_STORE = []


def publish(source, event_type, payload):

    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "event_type": event_type,
        "payload": payload
    }

    EVENT_STORE.append(event)

    return event


def get_events():

    return EVENT_STORE
