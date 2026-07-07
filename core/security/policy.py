POLICIES = {
    "NO_SCAN_NO_MOVE": True,
    "HUMAN_APPROVAL_REQUIRED": True,
    "CUSTOMER_DATA_PROTECTION": True
}

def check_policy(action):
    if action == "inventory_move" and POLICIES["NO_SCAN_NO_MOVE"]:
        return {
            "allowed": False,
            "reason": "Barcode scan required"
        }

    return {
        "allowed": True,
        "reason": "Policy approved"
    }
