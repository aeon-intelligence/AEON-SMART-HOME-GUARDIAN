from enterprise_knowledge.registry.knowledge_registry import KnowledgeRegistry
from enterprise_knowledge.memory.sop_memory import SOPMemory
from enterprise_knowledge.memory.lessons_learned import LessonsLearned
from enterprise_knowledge.retrieval.knowledge_search import search_knowledge


registry = KnowledgeRegistry()

knowledge = registry.register(
    "Inventory Risk Response",
    "Operations",
    "Verify stock, analyze demand, request approval"
)

sop = SOPMemory().store(
    "Inventory Adjustment",
    "Human approval required for high risk"
)

lesson = LessonsLearned().capture(
    "Stock Shortage Event",
    "Early detection reduces operational impact"
)

records = [
    knowledge,
    sop,
    lesson
]

print(search_knowledge(records, "risk"))
