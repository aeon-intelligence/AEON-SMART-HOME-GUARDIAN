from value_recovery_intelligence.shelf_life.shelf_monitor import monitor
from value_recovery_intelligence.demand.demand_forecast import forecast
from value_recovery_intelligence.waste.waste_predictor import predict
from value_recovery_intelligence.recovery.recovery_optimizer import optimize
from value_recovery_intelligence.memory.circular_memory import save


shelf = monitor(
    "SKU_FRESH_FOOD",
    2
)

demand = forecast(
    "SKU_FRESH_FOOD"
)

waste = predict(
    500
)

recovery = optimize(
    shelf
)

print(shelf)
print(demand)
print(waste)
print(recovery)
print(save(recovery))
