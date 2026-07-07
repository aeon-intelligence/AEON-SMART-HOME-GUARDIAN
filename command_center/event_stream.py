"""
AEON MATRIX Real-Time Event Stream
"""

from datetime import datetime
import uuid

EVENTS = []


def publish_event(event_type, payload):

    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "payload": payload
    }

    EVENTS.append(event)

    return event


def get_events():

    return EVENTS
