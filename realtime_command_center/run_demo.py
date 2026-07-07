from realtime_command_center.telemetry.telemetry_collector import collect
from realtime_command_center.event.event_processor import process
from realtime_command_center.status.status_engine import monitor
from realtime_command_center.decision.decision_router import route
from realtime_command_center.memory.live_memory import save


telemetry = collect(
    "ENTERPRISE_TELEMETRY_BUS"
)

event = process(
    "OPERATION_EVENT"
)

status = monitor(
    [
        telemetry,
        event
    ]
)

decision = route(
    status
)

print(telemetry)
print(event)
print(status)
print(decision)
print(save(decision))
