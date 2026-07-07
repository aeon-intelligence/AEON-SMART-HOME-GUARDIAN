from predictive_maintenance.asset.asset_registry import register
from predictive_maintenance.health.health_predictor import predict
from predictive_maintenance.planning.maintenance_planner import schedule
from predictive_maintenance.risk.failure_risk import analyze
from predictive_maintenance.memory.asset_memory import save


asset = register(
    "WAREHOUSE_CONVEYOR_01",
    "LOGISTICS_EQUIPMENT"
)

health = predict(
    asset
)

maintenance = schedule(
    health
)

risk = analyze(
    health
)

print(asset)
print(health)
print(maintenance)
print(risk)
print(save(risk))
