from customer_market_intelligence.signal.customer_signal import analyze
from customer_market_intelligence.trend.market_trend import detect
from customer_market_intelligence.behavior.consumer_behavior import evaluate
from customer_market_intelligence.opportunity.opportunity_engine import discover
from customer_market_intelligence.memory.customer_memory import save


signal = analyze(
    "CUSTOMER_PURCHASE_PATTERN"
)

trend = detect(
    "RETAIL_MARKET"
)

behavior = evaluate(
    "CONSUMER_BEHAVIOR_SIGNAL"
)

opportunity = discover(
    signal
)

print(signal)
print(trend)
print(behavior)
print(opportunity)
print(save(opportunity))
