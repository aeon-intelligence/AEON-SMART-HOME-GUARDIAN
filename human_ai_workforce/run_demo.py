from human_ai_workforce.signal.workforce_signal import analyze
from human_ai_workforce.skill.skill_engine import evaluate
from human_ai_workforce.agent.ai_collaboration import collaborate
from human_ai_workforce.optimization.workforce_optimizer import optimize
from human_ai_workforce.memory.workforce_memory import save


workforce = analyze(
    "ENTERPRISE_TEAM_SIGNAL"
)

skill = evaluate(
    "DIGITAL_OPERATION_SKILL"
)

agent = collaborate(
    "GUARDIAN_AI_AGENT"
)

optimization = optimize(
    [
        workforce,
        skill,
        agent
    ]
)

print(workforce)
print(skill)
print(agent)
print(optimization)
print(save(optimization))
