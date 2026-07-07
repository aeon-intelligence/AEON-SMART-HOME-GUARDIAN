from innovation_intelligence.idea.idea_engine import generate
from innovation_intelligence.experiment.experiment_manager import run
from innovation_intelligence.evaluation.outcome_evaluator import evaluate
from innovation_intelligence.learning.feedback_loop import learn
from innovation_intelligence.memory.innovation_memory import save


idea = generate(
    "WAREHOUSE_AUTOMATION"
)

experiment = run(
    idea
)

outcome = evaluate(
    experiment
)

learning = learn(
    outcome
)

print(idea)
print(experiment)
print(outcome)
print(learning)
print(save(learning))
