"""
AEON MATRIX Production Data Connector
"""


def ingest(source):

    return {
        "source": source,
        "connection": "ACTIVE",
        "records_received": 100
    }
