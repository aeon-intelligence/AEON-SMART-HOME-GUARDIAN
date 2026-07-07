from cognitive_command_center.dashboard.executive_dashboard import generate
from cognitive_command_center.signal.signal_aggregator import aggregate
from cognitive_command_center.kpi.kpi_engine import analyze
from cognitive_command_center.decision.decision_feed import generate as decision
from cognitive_command_center.memory.command_memory import save


dashboard = generate(
    "ALL_SYSTEMS_OPERATIONAL"
)

signals = aggregate(
    [
        "INVENTORY_SIGNAL",
        "MARKET_SIGNAL",
        "RISK_SIGNAL"
    ]
)

kpi = analyze(
    [
        "OTIF",
        "COST",
        "PRODUCTIVITY"
    ]
)

recommendation = decision(
    kpi
)

print(dashboard)
print(signals)
print(kpi)
print(recommendation)
print(save(recommendation))
