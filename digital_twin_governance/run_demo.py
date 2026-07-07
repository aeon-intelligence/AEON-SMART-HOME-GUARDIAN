from digital_twin_governance.state.twin_state import create_state
from digital_twin_governance.simulation.simulation_engine import simulate_change
from digital_twin_governance.governance.governance_check import validate
from digital_twin_governance.impact.impact_engine import analyze
from digital_twin_governance.memory.twin_memory import save


state = create_state(
    "AEON WMS",
    {
        "inventory_accuracy": 96,
        "service_level": 98
    }
)

simulation = simulate_change(
    state,
    "OPTIMIZE_ROUTE_ALLOCATION"
)

governance = validate(simulation)

impact = analyze(simulation)

print(state)
print(simulation)
print(governance)
print(impact)
print(save(impact))
