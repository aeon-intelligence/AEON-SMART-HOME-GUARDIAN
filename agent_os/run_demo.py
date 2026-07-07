from agent_os.lifecycle.agent_lifecycle import AgentLifecycle
from agent_os.health.agent_health import check_health
from agent_os.permission.permission_control import grant_permission
from agent_os.tasks.task_registry import TaskRegistry
from agent_os.evaluation.performance_score import evaluate


agent = AgentLifecycle().create(
    "Forecast Agent",
    "Demand Intelligence"
)

print(check_health(agent))

print(
    grant_permission(
        agent["agent"],
        "ANALYZE_DEMAND"
    )
)

tasks = TaskRegistry()

print(
    tasks.assign(
        agent["agent"],
        "Forecast next demand cycle"
    )
)

print(
    evaluate(
        agent["agent"],
        95,
        92
    )
)
