from strategic_intelligence.goal.goal_engine import create_goal
from strategic_intelligence.forecast.forecast_engine import forecast
from strategic_intelligence.scenario.scenario_planner import create_scenario
from strategic_intelligence.evaluation.strategy_evaluator import evaluate
from strategic_intelligence.memory.strategy_memory import save


goal = create_goal(
    "SUPPLY_CHAIN_EXCELLENCE",
    "OTIF_IMPROVEMENT"
)

forecast_result = forecast(
    "OPERATIONAL_EFFICIENCY"
)

scenario = create_scenario(
    "MARKET_VOLATILITY"
)

evaluation = evaluate(
    goal,
    forecast_result
)

print(goal)
print(forecast_result)
print(scenario)
print(evaluation)
print(save(evaluation))
