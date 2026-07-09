class EventBus:

    def publish(self, event):
        print(f"[EVENT] {event}")

    def subscribe(self, name):
        pass
