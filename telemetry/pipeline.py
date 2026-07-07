"""
AEON MATRIX Telemetry Pipeline
"""


from telemetry.event_bus import publish
from telemetry.event_processor import process


def ingest(event):

    publish_result = publish(event)
    analysis = process(event)

    return {
        "ingestion": publish_result,
        "analysis": analysis
    }
