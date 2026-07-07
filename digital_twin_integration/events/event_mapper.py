def map_event(event):

    event_type = event.get(
        "type",
        "UNKNOWN"
    )

    mapping = {

        "STOCK_SHORTAGE":
            "INVENTORY_RISK",

        "DELIVERY_DELAY":
            "TRANSPORT_RISK",

        "ORDER_SPIKE":
            "DEMAND_PRESSURE"
    }

    return {
        "original_event": event_type,
        "mapped_signal":
            mapping.get(
                event_type,
                "GENERAL_SIGNAL"
            )
    }
