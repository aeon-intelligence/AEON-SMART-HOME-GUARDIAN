class ObservabilityService:
    def record(self, event):
        return {
            "trace_id": event.get("trace_id"),
            "status": "recorded"
        }
