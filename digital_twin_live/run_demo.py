from digital_twin_live.state.twin_state import update
from digital_twin_live.sync.live_sync import synchronize
from digital_twin_live.simulation.live_simulator import simulate
from digital_twin_live.impact.live_impact import analyze
from digital_twin_live.memory.twin_memory import save


state = update(
    "AEON_WAREHOUSE",
    "OPERATIONAL"
)

sync = synchronize(
    "INVENTORY_TELEMETRY"
)

simulation = simulate(
    "DEMAND_SPIKE_25_PERCENT"
)

impact = analyze(
    simulation
)

print(state)
print(sync)
print(simulation)
print(impact)
print(save(impact))
