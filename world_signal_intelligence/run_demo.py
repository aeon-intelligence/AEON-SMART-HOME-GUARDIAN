from world_signal_intelligence.collector.signal_collector import collect_signal
from world_signal_intelligence.supply_chain.risk_analyzer import analyze_risk
from world_signal_intelligence.economy.economic_monitor import monitor_economy
from world_signal_intelligence.simulation.impact_simulator import simulate
from world_signal_intelligence.memory.future_memory import save


signal = collect_signal(
    "GLOBAL_MONITOR",
    "SUPPLY_CHAIN_DISRUPTION"
)

risk = analyze_risk(
    signal
)

economy = monitor_economy(
    "MARKET_PRESSURE"
)

impact = simulate(
    "LOGISTICS_DELAY"
)

print(signal)
print(risk)
print(economy)
print(impact)
print(save(impact))
