from human_ai_workforce.signals.workforce_signal import collect_signal
from human_ai_workforce.adoption.adoption_engine import calculate_adoption
from human_ai_workforce.skill.skill_engine import analyze_skill
from human_ai_workforce.collaboration.collaboration_engine import analyze_collaboration
from human_ai_workforce.memory.workforce_memory import save


signal = collect_signal(
    "OPERATIONS_TEAM",
    "AI_ASSISTED_DECISION"
)

adoption = calculate_adoption(
    92
)

skill = analyze_skill(
    "AI_WORKFLOW_OPERATION"
)

collaboration = analyze_collaboration(
    signal
)

print(signal)
print(adoption)
print(skill)
print(collaboration)
print(save(collaboration))
