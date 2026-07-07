def classify(data):

    sensitive_words = [
        "FINANCE",
        "CUSTOMER",
        "SECRET"
    ]

    level = "INTERNAL"

    for word in sensitive_words:
        if word in data.upper():
            level = "RESTRICTED"

    return {
        "data": data,
        "classification": level
    }
