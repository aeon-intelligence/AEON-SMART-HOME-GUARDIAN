from alert_intelligence.engine.alert_engine import create
from alert_intelligence.priority.priority_engine import calculate
from alert_intelligence.correlation.signal_correlation import analyze
from alert_intelligence.notification.notification_router import route
from alert_intelligence.escalation.escalation_engine import escalate
from alert_intelligence.memory.alert_memory import save


signal = {
    "event": "INVENTORY_RISK",
    "risk_score": 91,
    "source": "TELEMETRY_HUB"
}


alert = create(signal)

priority = calculate(alert)

correlation = analyze(
    [signal, alert]
)

notification = route(alert)

escalation = escalate(alert)

memory = save(
    {
        "alert": alert,
        "priority": priority,
        "correlation": correlation,
        "notification": notification,
        "escalation": escalation
    }
)


print(alert)
print(priority)
print(correlation)
print(notification)
print(escalation)
print(memory)
