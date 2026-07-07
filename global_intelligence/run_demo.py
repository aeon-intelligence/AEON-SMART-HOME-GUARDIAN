from global_intelligence.collector.global_signal import collect
from global_intelligence.analyzer.future_analyzer import analyze
from global_intelligence.impact.impact_engine import evaluate
from global_intelligence.preparedness.action_engine import recommend
from global_intelligence.memory.future_memory import save


signal = collect(
    "GLOBAL_TECHNOLOGY_ECONOMIC_SIGNAL"
)

analysis = analyze(
    signal
)

impact = evaluate(
    analysis
)

action = recommend(
    impact
)

print(signal)
print(analysis)
print(impact)
print(action)
print(save(action))
