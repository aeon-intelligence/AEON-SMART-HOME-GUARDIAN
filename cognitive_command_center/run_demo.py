from cognitive_command_center.telemetry.signal_fusion import collect_signals
from cognitive_command_center.kpi.kpi_engine import analyze_kpi
from cognitive_command_center.risk.risk_engine import analyze_risk
from cognitive_command_center.decision.decision_engine import recommend
from cognitive_command_center.alert.alert_engine import generate_alert
from cognitive_command_center.memory.decision_memory import save


signals = collect_signals(
    "ENTERPRISE_TELEMETRY",
    "OPERATION_STATUS"
)

kpi = analyze_kpi(
    "OTIF_PRODUCTIVITY_PROFIT"
)

risk = analyze_risk(
    signals
)

decision = recommend(
    kpi,
    risk
)

alert = generate_alert(
    risk["risk_level"]
)

print(signals)
print(kpi)
print(risk)
print(decision)
print(alert)
print(save(decision))
