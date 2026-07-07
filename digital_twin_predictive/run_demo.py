from digital_twin_predictive.entity.twin_entity import create_entity
from digital_twin_predictive.simulation.simulation_engine import simulate
from digital_twin_predictive.impact.impact_analyzer import analyze
from digital_twin_predictive.prediction.predictive_engine import predict
from digital_twin_predictive.memory.simulation_memory import save


warehouse = create_entity(
    "MAIN_WAREHOUSE",
    "LOGISTICS_NODE"
)

simulation = simulate(
    warehouse,
    "DEMAND_SPIKE"
)

impact = analyze(
    simulation
)

prediction = predict(
    impact
)

print(warehouse)
print(simulation)
print(impact)
print(prediction)
print(save(prediction))
