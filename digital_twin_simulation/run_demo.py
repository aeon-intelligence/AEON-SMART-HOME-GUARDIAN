from digital_twin_simulation.model.twin_model import create
from digital_twin_simulation.scenario.scenario_engine import simulate
from digital_twin_simulation.impact.impact_analyzer import analyze
from digital_twin_simulation.prediction.future_predictor import predict
from digital_twin_simulation.memory.simulation_memory import save


twin = create(
    "AEON_WAREHOUSE_OPERATION"
)

scenario = simulate(
    "DEMAND_INCREASE_30_PERCENT"
)

impact = analyze(
    scenario
)

prediction = predict(
    impact
)

print(twin)
print(scenario)
print(impact)
print(prediction)
print(save(prediction))
