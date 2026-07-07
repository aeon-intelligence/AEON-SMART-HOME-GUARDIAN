from economic_intelligence.value.value_analyzer import analyze_value
from economic_intelligence.cost.cost_optimizer import optimize_cost
from economic_intelligence.revenue.revenue_detector import detect_opportunity
from economic_intelligence.decision.business_decision import create_decision
from economic_intelligence.memory.value_memory import save


value = analyze_value(
    "AUTONOMOUS_ROUTE_OPTIMIZATION"
)

cost = optimize_cost(
    "LOGISTICS_RESOURCE"
)

revenue = detect_opportunity(
    "CUSTOMER_DEMAND_SIGNAL"
)

decision = create_decision(
    value,
    cost,
    revenue
)

print(value)
print(cost)
print(revenue)
print(decision)
print(save(decision))
