def safe_view(data):
    if isinstance(data, dict):
        return {
            key: "***REDACTED***"
            if key.lower() in ("secret", "key", "token", "password")
            else safe_view(value)
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [safe_view(item) for item in data]

    return data


def main():
    memory = {
        "identity": "AEON-USER",
        "secret": "hidden-secret",
        "key": "hidden-key"
    }

    print("=== IDENTITY MEMORY ===")
    print(safe_view(memory))


if __name__ == "__main__":
    main()
