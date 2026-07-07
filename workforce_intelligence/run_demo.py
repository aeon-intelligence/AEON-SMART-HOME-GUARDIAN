from workforce_intelligence.skills.skill_analyzer import analyze_skill
from workforce_intelligence.coach.work_coach import AIWorkCoach
from workforce_intelligence.learning.learning_path import create_learning_path
from workforce_intelligence.signals.adoption_signal import create_adoption_signal


employee = {
    "ai_usage": 30
}

skill = analyze_skill(employee)

coach = AIWorkCoach()

print(
    coach.analyze(
        {
            "skill_gap": skill
        }
    )
)

print(create_learning_path(skill))

print(create_adoption_signal(70))
