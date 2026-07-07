from digital_twin_integration.state.twin_state import EnterpriseTwinState


class TwinSyncEngine:

    def __init__(self):

        self.state = EnterpriseTwinState()


    def update(self, signal):

        if signal == "INVENTORY_RISK":
            self.state.inventory_health -= 20
            self.state.operational_risk += 30

        return self.state
