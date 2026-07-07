"""
AEON MATRIX Consensus Decision Engine
"""


def evaluate_consensus(inputs):

    confidence = sum(inputs) / len(inputs)

    if confidence >= 80:
        decision = "APPROVED"
    else:
        decision = "REVIEW_REQUIRED"

    return {
        "consensus": decision,
        "confidence": round(confidence,2)
    }
