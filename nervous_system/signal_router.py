"""
AEON MATRIX Signal Router
"""


def route_signal(event):

    event_type = event.get("event_type")

    if event_type in [
        "INVENTORY_RISK",
        "ORDER_DELAY",
        "STOCK_SHORTAGE"
    ]:
        destination = "GUARDIAN_AGENT"

    elif event_type in [
        "MARKET_SIGNAL",
        "CUSTOMER_SIGNAL"
    ]:
        destination = "INSIGHT_ENGINE"

    else:
        destination = "TELEMETRY_ARCHIVE"

    return {
        "event_type": event_type,
        "route": destination
    }
