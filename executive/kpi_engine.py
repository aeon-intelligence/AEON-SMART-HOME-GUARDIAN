"""
AEON MATRIX KPI Snapshot Engine
"""

from datetime import datetime


def generate_kpi_snapshot(metrics):

    inventory = metrics.get("inventory_health", 100)
    sla = metrics.get("sla_score", 100)
    productivity = metrics.get("productivity", 100)

    health = round(
        (inventory + sla + productivity) / 3,
        2
    )

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "system_health": health,
        "inventory_health": inventory,
        "sla_score": sla,
        "productivity": productivity
    }
