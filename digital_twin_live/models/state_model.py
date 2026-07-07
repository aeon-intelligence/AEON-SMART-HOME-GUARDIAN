from dataclasses import dataclass


@dataclass
class TwinState:
    inventory_risk: int = 0
    operational_health: int = 100
    market_pressure: int = 0
