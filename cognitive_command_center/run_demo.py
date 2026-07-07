from cognitive_command_center.signals.signal_aggregator import collect_signal
from cognitive_command_center.kpi.kpi_engine import calculate_kpi
from cognitive_command_center.risk.risk_engine import analyze_risk
from cognitive_command_center.decision.decision_view import create_decision_view
from cognitive_command_center.memory.command_memory import save


signal = collect_signal(
    "SUPPLY_CHAIN_HEALTH",
    91
)

kpi = calculate_kpi(
    {
        "otif": 97,
        "productivity": 94,
        "accuracy": 98
    }
)

risk = analyze_risk(signal)

decision = create_decision_view(
    kpi,
    risk
)

print(signal)
print(kpi)
print(risk)
print(decision)
print(save(decision))
