from global_intelligence.collector.signal_collector import collect
from global_intelligence.analysis.world_analyzer import analyze
from global_intelligence.classification.signal_classifier import classify
from global_intelligence.preparedness.future_engine import prepare
from global_intelligence.memory.global_memory import save


signal = collect(
    "WORLD_SIGNAL_AGENT",
    "SUPPLY_CHAIN_DISRUPTION"
)

analysis = analyze(
    signal
)

classification = classify(
    "SUPPLY_CHAIN_RISK"
)

prepared = prepare(
    analysis
)

print(signal)
print(analysis)
print(classification)
print(prepared)
print(save(prepared))
