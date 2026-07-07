from cognitive_command_center.context.context_engine import analyze
from cognitive_command_center.insight.insight_generator import generate
from cognitive_command_center.decision.decision_engine import recommend
from cognitive_command_center.dashboard.command_dashboard import display
from cognitive_command_center.memory.cognitive_memory import save


context = analyze(
    "ENTERPRISE_REALTIME_OPERATION"
)

insight = generate(
    context
)

decision = recommend(
    insight
)

dashboard = display(
    decision
)

print(context)
print(insight)
print(decision)
print(dashboard)
print(save(dashboard))
