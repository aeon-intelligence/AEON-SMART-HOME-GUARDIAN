def monitor(sku, days_left):

    return {
        "sku": sku,
        "days_left": days_left,
        "status":
            "RISK"
            if days_left < 3
            else "SAFE"
    }
