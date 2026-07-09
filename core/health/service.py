class HealthService:
    def status(self):
        return {
            "runtime": "HEALTHY",
            "event_bus": "HEALTHY",
            "orchestrator": "HEALTHY",
            "telemetry": "HEALTHY"
        }
