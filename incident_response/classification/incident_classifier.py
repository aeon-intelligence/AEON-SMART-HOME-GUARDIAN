def classify(event):

    if event.get("severity") == "HIGH":
        category = "CRITICAL_OPERATION"

    else:
        category = "NORMAL_OPERATION"

    return {
        "event": event["name"],
        "category": category
    }
