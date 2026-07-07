from human_ai_collaboration.workforce.workforce_engine import analyze
from human_ai_collaboration.skill.skill_mapper import map_skill
from human_ai_collaboration.assignment.task_assignment import assign
from human_ai_collaboration.monitor.collaboration_monitor import monitor
from human_ai_collaboration.memory.workforce_memory import save


team = analyze(
    "WAREHOUSE_OPERATION_TEAM"
)

skill = map_skill(
    "OPERATION_MANAGER"
)

assignment = assign(
    "INVENTORY_DECISION_REVIEW",
    "HUMAN_SUPERVISOR"
)

collaboration = monitor(
    assignment
)

print(team)
print(skill)
print(assignment)
print(collaboration)
print(save(collaboration))
