from digital_twin_simulation.scenario.scenario_engine import create_scenario
from digital_twin_simulation.forecast.impact_forecast import forecast
from digital_twin_simulation.compare.decision_compare import compare
from digital_twin_simulation.engine.simulation_core import run_simulation
from digital_twin_simulation.memory.simulation_memory import save


scenario = create_scenario(
    "SUPPLY_CHAIN_DELAY",
    "TRANSPORT_DISRUPTION"
)

impact = forecast(
    scenario
)

decision = compare(
    [
        "OPTION_A",
        "OPTION_B"
    ]
)

simulation = run_simulation(
    decision
)

print(scenario)
print(impact)
print(decision)
print(simulation)
print(save(simulation))
