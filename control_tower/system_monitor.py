"""
AEON MATRIX System Health Monitor
"""

from datetime import datetime


def system_health(components):

    online = sum(
        1 for c in components
        if c.get("status") == "ONLINE"
    )

    score = round(
        (online / len(components)) * 100,
        2
    )

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "health_score": score,
        "status": "HEALTHY" if score >= 80 else "WARNING"
    }
