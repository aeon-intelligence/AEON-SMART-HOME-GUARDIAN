from telemetry_intelligence_bus.event.event_bus import publish
from telemetry_intelligence_bus.collector.signal_collector import collect
from telemetry_intelligence_bus.analysis.signal_analyzer import analyze
from telemetry_intelligence_bus.monitor.health_monitor import check
from telemetry_intelligence_bus.memory.telemetry_memory import save


event = publish(
    "INVENTORY_UPDATED"
)

signal = collect(
    "WMS",
    "STOCK_LEVEL"
)

analysis = analyze(
    signal
)

health = check(
    "AEON_MATRIX_CORE"
)

print(event)
print(signal)
print(analysis)
print(health)
print(save(health))
