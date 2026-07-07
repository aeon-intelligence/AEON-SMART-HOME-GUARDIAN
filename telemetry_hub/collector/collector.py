from telemetry_hub.bus.event_bus import EventBus


class TelemetryCollector:

    def __init__(self):
        self.bus = EventBus()

    def collect(self, source, payload):

        return self.bus.publish(
            {
                "source": source,
                "payload": payload
            }
        )
