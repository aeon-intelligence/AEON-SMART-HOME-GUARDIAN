from datetime import datetime


class SystemHealthMonitor:

    def check(self, metrics):

        status = (
            "HEALTHY"
            if metrics["score"] >= 80
            else "DEGRADED"
        )

        return {
            "status": status,
            "health_score": metrics["score"],
            "timestamp":
                datetime.utcnow().isoformat()
        }
