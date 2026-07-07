from observability_sre.metrics.metrics_engine import collect_metrics
from observability_sre.health.service_health import check_service
from observability_sre.incident.incident_detector import detect_incident
from observability_sre.reliability.reliability_score import calculate_score
from observability_sre.recovery.recovery_signal import create_recovery_signal


metrics = collect_metrics(
    "AEON MATRIX CORE"
)

incident = detect_incident(
    metrics
)

print(metrics)
print(check_service(metrics))
print(incident)
print(calculate_score(metrics))
print(create_recovery_signal(incident))
