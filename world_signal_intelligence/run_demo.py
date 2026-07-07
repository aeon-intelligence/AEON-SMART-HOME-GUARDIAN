from world_signal_intelligence.collector.signal_collector import collect
from world_signal_intelligence.analysis.trend_analyzer import analyze
from world_signal_intelligence.risk.future_risk_detector import detect
from world_signal_intelligence.opportunity.opportunity_engine import identify
from world_signal_intelligence.memory.signal_memory import save


signal = collect(
    "GLOBAL_MARKET",
    "AI_SUPPLY_CHAIN_TRANSFORMATION"
)

trend = analyze(
    signal
)

risk = detect(
    trend
)

opportunity = identify(
    signal
)

print(signal)
print(trend)
print(risk)
print(opportunity)
print(save(opportunity))
