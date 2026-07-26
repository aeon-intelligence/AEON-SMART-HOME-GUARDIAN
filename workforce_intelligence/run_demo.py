from workforce_intelligence.skills.skill_analyzer import analyze_skill
from workforce_intelligence.coach.work_coach import AIWorkCoach
from workforce_intelligence.learning.learning_path import create_learning_path
from workforce_intelligence.signals.adoption_signal import create_adoption_signal


employee = {
    "ai_usage": 30
}


skill = analyze_skill(employee)

coach = AIWorkCoach()


analysis = coach.analyze({
    "skill_gap": skill
})

learning = create_learning_path(skill)

signal = create_adoption_signal(70)


print({
    "skill_analysis": "COMPLETED",
    "coach_analysis": "COMPLETED",
    "learning_path": "GENERATED",
    "adoption_signal": "RECORDED"
})
