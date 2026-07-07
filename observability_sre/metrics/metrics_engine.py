from datetime import datetime


def collect_metrics(system):

    return {
        "system": system,
        "cpu_usage": 45,
        "memory_usage": 52,
        "latency_ms": 120,
        "timestamp":
            datetime.utcnow().isoformat()
    }
