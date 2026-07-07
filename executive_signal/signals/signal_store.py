import json


def save_signal(signal):

    with open(
        "executive_signal/signals/executive_signals.json",
        "a"
    ) as file:
        file.write(json.dumps(signal) + "\n")

    return signal
