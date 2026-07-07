from self_healing_engine.health.health_monitor import check_health
from self_healing_engine.failure.failure_predictor import predict_failure
from self_healing_engine.recovery.recovery_engine import recover
from self_healing_engine.reliability.reliability_score import calculate
from self_healing_engine.memory.incident_memory import save


health = check_health(
    "AEON CORE SERVICES",
    96
)

failure = predict_failure(
    health
)

recovery = recover(
    failure["prediction"]
)

reliability = calculate(
    96
)

print(health)
print(failure)
print(recovery)
print(reliability)
print(save(recovery))
