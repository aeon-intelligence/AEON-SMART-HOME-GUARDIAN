"""
Observability Alert Rules
"""


ALERT_RULES = {
    "HIGH_LATENCY": "latency_ms > 1000",
    "HIGH_ERROR_RATE": "error_rate > 5",
    "SERVICE_FAILURE": "service_unavailable"
}
