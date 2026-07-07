from digital_twin_live.models.state_model import TwinState
from digital_twin_live.telemetry.twin_events import create_twin_event


class DigitalTwinEngine:

    def __init__(self):
        self.state = TwinState()

    def update(self, inventory_risk, market_pressure):
        self.state.inventory_risk = inventory_risk
        self.state.market_pressure = market_pressure

        return create_twin_event(
            "DIGITAL_TWIN_STATE_UPDATED",
            {
                "inventory_risk": inventory_risk,
                "market_pressure": market_pressure,
                "operational_health": self.state.operational_health
            }
        )


if __name__ == "__main__":
    engine = DigitalTwinEngine()

    print(
        engine.update(
            inventory_risk=35,
            market_pressure=20
        )
    )
