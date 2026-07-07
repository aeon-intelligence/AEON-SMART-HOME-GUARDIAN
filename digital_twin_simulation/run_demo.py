from digital_twin_simulation.scenario.scenario_generator import ScenarioGenerator
from digital_twin_simulation.engine.simulator import ScenarioSimulator
from digital_twin_simulation.risk.risk_engine import calculate_risk
from digital_twin_simulation.prediction.future_prediction import predict


scenario = ScenarioGenerator().create(
    "DEMAND_SPIKE_SIMULATION",
    {
        "inventory": 500,
        "demand": 900
    }
)

simulation = ScenarioSimulator().run(
    scenario
)

risk = calculate_risk(
    simulation
)

future = predict(
    risk
)

print(scenario)
print(simulation)
print(risk)
print(future)
