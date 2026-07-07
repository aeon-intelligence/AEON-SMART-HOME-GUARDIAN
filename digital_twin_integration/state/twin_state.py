from dataclasses import dataclass


@dataclass
class EnterpriseTwinState:

    inventory_health: int = 100
    delivery_health: int = 100
    operational_risk: int = 0
