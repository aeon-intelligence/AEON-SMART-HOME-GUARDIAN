from dataclasses import dataclass


@dataclass
class SystemState:
    system_health: int = 100
    active_risk: int = 0
    critical_alerts: int = 0
