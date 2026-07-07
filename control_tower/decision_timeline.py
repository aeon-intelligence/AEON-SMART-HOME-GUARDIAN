"""
AEON MATRIX Decision Timeline
"""

from datetime import datetime


def record_decision(source, decision):

    return {
        "time": datetime.utcnow().isoformat(),
        "source": source,
        "decision": decision
    }
