from digital_twin_intelligence.model.twin_model import create
from digital_twin_intelligence.simulation.scenario_simulator import simulate
from digital_twin_intelligence.prediction.impact_predictor import predict
from digital_twin_intelligence.evaluation.simulation_evaluator import evaluate
from digital_twin_intelligence.memory.twin_memory import save


twin = create(
    "ENTERPRISE_OPERATION_MODEL"
)

simulation = simulate(
    "SUPPLY_CHAIN_OPTIMIZATION"
)

prediction = predict(
    simulation
)

evaluation = evaluate(
    prediction
)

print(twin)
print(simulation)
print(prediction)
print(evaluation)
print(save(evaluation))
