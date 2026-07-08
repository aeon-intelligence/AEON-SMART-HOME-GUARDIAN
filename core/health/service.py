SERVICES = [
    "TMS",
    "WMS",
    "ERP",
    "GPS",
    "Telemetry",
    "EventBus"
]

def health():
    return {
        service: "HEALTHY"
        for service in SERVICES
    }
