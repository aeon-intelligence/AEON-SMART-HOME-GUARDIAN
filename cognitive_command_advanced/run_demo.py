from cognitive_command_advanced.context.context_engine import understand
from cognitive_command_advanced.reasoning.impact_reasoning import analyze
from cognitive_command_advanced.insight.executive_insight import generate
from cognitive_command_advanced.decision.decision_layer import decide
from cognitive_command_advanced.memory.cognitive_memory import save


context = understand(
    "SUPPLY_CHAIN_RISK_EVENT"
)

impact = analyze(
    context
)

insight = generate(
    impact
)

decision = decide(
    insight
)

print(context)
print(impact)
print(insight)
print(decision)
print(save(decision))
