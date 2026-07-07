from datetime import datetime


class EventBus:

    def __init__(self):
        self.events = []


    def publish(self, event_type, payload):

        event = {
            "event_type": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(event)

        return event


    def get_events(self):

        return self.events
