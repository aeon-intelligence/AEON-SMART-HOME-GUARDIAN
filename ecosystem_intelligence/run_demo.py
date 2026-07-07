from ecosystem_intelligence.partner.partner_engine import analyze
from ecosystem_intelligence.signal.external_signal import detect
from ecosystem_intelligence.relationship.ecosystem_graph import connect
from ecosystem_intelligence.insight.ecosystem_insight import generate
from ecosystem_intelligence.memory.ecosystem_memory import save


partner = analyze(
    "LOGISTICS_PARTNER"
)

signal = detect(
    "MARKET_TECHNOLOGY_CHANGE"
)

relation = connect(
    "AEON_MATRIX",
    "PARTNER_NETWORK"
)

insight = generate(
    [
        partner,
        signal,
        relation
    ]
)

print(partner)
print(signal)
print(relation)
print(insight)
print(save(insight))
