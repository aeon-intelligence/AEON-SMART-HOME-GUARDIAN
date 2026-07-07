from knowledge_evolution.registry.knowledge_registry import KnowledgeRegistry
from knowledge_evolution.sop.sop_engine import analyze_sop
from knowledge_evolution.lessons.lesson_memory import store_lesson
from knowledge_evolution.best_practice.best_practice import generate_best_practice
from knowledge_evolution.retrieval.knowledge_search import search


registry = KnowledgeRegistry()

registry.add(
    "Inventory Control SOP",
    "OPERATIONS",
    "No Scan No Move policy"
)

print(
    analyze_sop(
        "Inventory Adjustment"
    )
)

lesson = store_lesson(
    "Stock Incident",
    "Require Guardian Review"
)

print(lesson)

print(
    generate_best_practice(
        lesson
    )
)

print(
    search(
        "Scan",
        registry.knowledge
    )
)
