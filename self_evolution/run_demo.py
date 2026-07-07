from self_evolution.outcome.outcome_collector import collect
from self_evolution.learning.learning_engine import learn
from self_evolution.improvement.improvement_core import improve
from self_evolution.policy.policy_evolution import evolve
from self_evolution.memory.evolution_memory import save


outcome = collect(
    "OPERATION_RESULT"
)

learning = learn(
    outcome
)

improvement = improve(
    learning
)

policy = evolve(
    improvement
)

print(outcome)
print(learning)
print(improvement)
print(policy)
print(save(policy))
