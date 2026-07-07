from operations_control_tower.monitor.state_monitor import monitor_state
from operations_control_tower.sla.sla_guard import check_sla
from operations_control_tower.resource.resource_allocator import allocate_resource
from operations_control_tower.workflow.autonomous_workflow import trigger_workflow
from operations_control_tower.memory.operation_memory import save


state = monitor_state(
    "AEON LOGISTICS",
    96
)

sla = check_sla(
    state["health_score"]
)

resource = allocate_resource(
    "HIGH"
)

workflow = trigger_workflow(
    sla["sla_status"]
)

print(state)
print(sla)
print(resource)
print(workflow)
print(save(workflow))
