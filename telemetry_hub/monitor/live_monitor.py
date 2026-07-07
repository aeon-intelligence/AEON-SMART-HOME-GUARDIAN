from telemetry_hub.collector.collector import TelemetryCollector


collector = TelemetryCollector()


event = collector.collect(
    "DIGITAL_TWIN",
    {
        "inventory_risk": 91,
        "market_pressure": 72
    }
)


print({
    "telemetry_status": "ACTIVE",
    "event": event
})
