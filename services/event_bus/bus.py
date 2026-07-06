from core.brain.memory import memory

class EventBus:
    def __init__(self):
        self.events = []

    def publish(self, event: dict):
        self.events.append(event)
        memory.add_event(event)
        return {"status": "received", "event": event}

    def get_all(self):
        return self.events

bus = EventBus()
