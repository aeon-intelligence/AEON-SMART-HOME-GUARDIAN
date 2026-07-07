from cognitive_memory.episode.episode_memory import store_event
from cognitive_memory.decision.decision_history import record_decision
from cognitive_memory.lesson.lesson_extractor import extract_lesson
from cognitive_memory.recall.pattern_recall import recall
from cognitive_memory.organization.org_memory import save


event = store_event(
    "INVENTORY_OPTIMIZATION",
    "WASTE_REDUCED"
)

decision = record_decision(
    "AUTO_REBALANCE_STOCK",
    "SUCCESS"
)

lesson = extract_lesson(
    decision
)

pattern = recall(
    "STOCK_OPTIMIZATION"
)

print(event)
print(decision)
print(lesson)
print(pattern)
print(save(lesson))
