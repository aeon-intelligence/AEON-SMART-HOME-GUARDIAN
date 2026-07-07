from workflow_intelligence.discovery.process_discovery import discover
from workflow_intelligence.generator.workflow_generator import generate
from workflow_intelligence.execution.task_executor import execute
from workflow_intelligence.monitor.workflow_monitor import monitor
from workflow_intelligence.memory.process_memory import save


process = discover(
    "ORDER_FULFILLMENT_PROCESS"
)

workflow = generate(
    process
)

execution = execute(
    workflow
)

health = monitor(
    execution
)

print(process)
print(workflow)
print(execution)
print(health)
print(save(health))
