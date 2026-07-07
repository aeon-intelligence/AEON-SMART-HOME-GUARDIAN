from autonomous_innovation.learning.outcome_learning import learn_outcome
from autonomous_innovation.discovery.pattern_discovery import discover_pattern
from autonomous_innovation.proposal.innovation_proposal import create_proposal
from autonomous_innovation.optimization.self_optimizer import optimize
from autonomous_innovation.memory.innovation_memory import save


learning = learn_outcome(
    "SLA_IMPROVED"
)

pattern = discover_pattern(
    learning
)

proposal = create_proposal(
    pattern
)

optimization = optimize(
    proposal
)

print(learning)
print(pattern)
print(proposal)
print(optimization)
print(save(optimization))
