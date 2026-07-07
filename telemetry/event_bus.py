"""
AEON MATRIX Enterprise Event Bus
"""


EVENT_STORE = []


def publish(event):

    EVENT_STORE.append(event)

    return {
        "published": True,
        "event_type": event.get("event_type")
    }


def get_events():

    return EVENT_STORE
