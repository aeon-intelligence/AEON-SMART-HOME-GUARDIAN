"""
AEON MATRIX Production Observability Engine
"""


class ObservabilityEngine:

    def collect(self, service: str, metrics: dict):

        return {
            "service": service,
            "status": "MONITORED",
            "metrics": metrics,
            "alert_required": self.detect_issue(metrics)
        }

    def detect_issue(self, metrics):

        if metrics.get("error_rate", 0) > 5:
            return True

        if metrics.get("latency_ms", 0) > 1000:
            return True

        return False
