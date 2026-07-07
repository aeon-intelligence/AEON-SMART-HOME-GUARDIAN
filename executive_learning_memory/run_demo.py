from executive_learning_memory.capture.experience_capture import capture
from executive_learning_memory.outcome.outcome_learning import learn
from executive_learning_memory.knowledge.knowledge_builder import consolidate
from executive_learning_memory.insight.executive_insight import generate
from executive_learning_memory.memory.organizational_memory import save


experience = capture(
    "INVENTORY_OPTIMIZATION_DECISION"
)

learning = learn(
    "WASTE_REDUCTION_SUCCESS"
)

knowledge = consolidate(
    [
        experience,
        learning
    ]
)

insight = generate(
    knowledge
)

print(experience)
print(learning)
print(knowledge)
print(insight)
print(save(insight))
