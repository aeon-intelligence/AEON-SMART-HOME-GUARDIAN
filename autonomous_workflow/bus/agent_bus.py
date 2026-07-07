def send_message(sender, receiver, message):

    return {
        "from": sender,
        "to": receiver,
        "message": message,
        "status": "DELIVERED"
    }
