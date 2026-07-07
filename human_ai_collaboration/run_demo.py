from human_ai_collaboration.interaction.interaction_monitor import monitor
from human_ai_collaboration.adoption.adoption_score import calculate_adoption
from human_ai_collaboration.skill.skill_gap import analyze_skill_gap
from human_ai_collaboration.learning.learning_recommendation import recommend
from human_ai_collaboration.memory.collaboration_memory import save


interaction = monitor(
    "warehouse_team",
    "AI_ASSISTED_DECISION"
)

adoption = calculate_adoption(
    "DAILY_USAGE"
)

skill = analyze_skill_gap(
    "AI_OPERATION"
)

learning = recommend(
    skill
)

print(interaction)
print(adoption)
print(skill)
print(learning)
print(save(learning))
