SIGNAL_TYPES = {

    "INVENTORY_RISK_SIGNAL":
        "Inventory risk detected",

    "DIGITAL_TWIN_UPDATE":
        "Digital Twin state changed",

    "EXECUTIVE_ALERT":
        "Executive attention required"
}


def register_signal(signal):

    return {
        "registered": True,
        "signal_type": signal
    }
