from financial_intelligence.revenue.revenue_analyzer import analyze
from financial_intelligence.cost.cost_optimizer import optimize
from financial_intelligence.profit.profit_engine import calculate
from financial_intelligence.roi.roi_engine import evaluate
from financial_intelligence.value.value_optimizer import optimize as value_optimize
from financial_intelligence.memory.financial_memory import save


revenue = analyze(
    500000
)

cost = optimize(
    200000
)

profit = calculate(
    [revenue, cost]
)

roi = evaluate(
    "AI_OPTIMIZATION_PROJECT"
)

value = value_optimize(
    profit
)

print(revenue)
print(cost)
print(profit)
print(roi)
print(value)
print(save(value))
