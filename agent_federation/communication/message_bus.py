def send(source, target, message):

    return {
        "from": source,
        "to": target,
        "message": message,
        "delivery": "SUCCESS"
    }
