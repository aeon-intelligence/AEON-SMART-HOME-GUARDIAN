from strategic_foresight.signal.world_signal import collect_signal
from strategic_foresight.risk.risk_forecast import forecast
from strategic_foresight.scenario.scenario_engine import simulate
from strategic_foresight.simulation.strategy_simulator import evaluate_strategy
from strategic_foresight.memory.foresight_memory import save_prediction


signal = collect_signal(
    "SUPPLY_CHAIN_PRESSURE",
    91
)

risk = forecast(signal)

scenario = simulate(
    "GLOBAL_SUPPLY_DISRUPTION",
    risk
)

strategy = evaluate_strategy(
    scenario
)

memory = save_prediction(
    strategy
)

print(signal)
print(risk)
print(scenario)
print(strategy)
print(memory)
