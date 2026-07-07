from telemetry_hub.collector.event_collector import collect
from telemetry_hub.processor.signal_processor import process
from telemetry_hub.router.event_router import route
from telemetry_hub.alert.cognitive_alert import generate
from telemetry_hub.memory.telemetry_memory import save


event = collect(
    "INVENTORY_RISK_EVENT"
)

signal = process(
    event
)

routing = route(
    signal
)

alert = generate(
    routing
)

print(event)
print(signal)
print(routing)
print(alert)
print(save(alert))
