from integration.event_bus.event_bus import EventBus
from integration.connectors.security_connector import send_security_event
from integration.connectors.intelligence_connector import send_intelligence_event
from integration.memory.integration_memory import save


bus = EventBus()


security_event = send_security_event(
    {
        "type": "SECURITY_ANOMALY",
        "risk_score": 87
    }
)


intelligence_event = send_intelligence_event(
    {
        "type": "FORECAST_SIGNAL",
        "confidence": 91
    }
)


event1 = bus.publish(
    "SECURITY_EVENT",
    security_event
)


event2 = bus.publish(
    "INTELLIGENCE_EVENT",
    intelligence_event
)


memory = save(
    bus.get_events()
)


print(event1)
print(event2)
print(memory)
