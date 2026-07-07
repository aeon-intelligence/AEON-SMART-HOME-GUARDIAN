def check_service(metrics):

    healthy = (
        metrics["latency_ms"] < 500
    )

    return {
        "service_status":
            "HEALTHY"
            if healthy
            else "DEGRADED"
    }
