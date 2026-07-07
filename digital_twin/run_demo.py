from digital_twin.model.twin_model import create
from digital_twin.scenario.scenario_engine import generate
from digital_twin.simulation.simulation_engine import run
from digital_twin.analysis.impact_analyzer import analyze
from digital_twin.memory.simulation_memory import save


twin = create(
    "AEON_WAREHOUSE_OPERATION"
)


scenario = generate(
    {
        "event": "STOCK_SHORTAGE",
        "risk": 85
    }
)


simulation = run(
    scenario
)


impact = analyze(
    simulation
)


memory = save(
    {
        "twin": twin,
        "scenario": scenario,
        "simulation": simulation,
        "impact": impact
    }
)


print(twin)
print(scenario)
print(simulation)
print(impact)
print(memory)
