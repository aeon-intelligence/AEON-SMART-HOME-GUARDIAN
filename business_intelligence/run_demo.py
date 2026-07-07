from business_intelligence.kpi.kpi_engine import analyze as kpi
from business_intelligence.revenue.revenue_analyzer import analyze as revenue
from business_intelligence.cost.cost_optimizer import analyze as cost
from business_intelligence.value.value_recovery import calculate
from business_intelligence.forecast.business_forecast import predict
from business_intelligence.insight.executive_insight import generate
from business_intelligence.memory.business_memory import save


operation = {
    "system": "AEON_MATRIX",
    "domain": "ENTERPRISE_OPERATION"
}


kpi_result = kpi(operation)
revenue_result = revenue(kpi_result)
cost_result = cost(revenue_result)
value_result = calculate(cost_result)
forecast_result = predict(value_result)
insight_result = generate(forecast_result)

memory = save({
    "kpi": kpi_result,
    "revenue": revenue_result,
    "cost": cost_result,
    "value": value_result,
    "forecast": forecast_result,
    "insight": insight_result
})


print(kpi_result)
print(revenue_result)
print(cost_result)
print(value_result)
print(forecast_result)
print(insight_result)
print(memory)
