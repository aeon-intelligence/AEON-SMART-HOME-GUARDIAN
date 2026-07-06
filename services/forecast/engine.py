def forecast_demand(base: int, trend: float):
    predicted = base * (1 + trend)

    risk = 0
    if predicted > 100:
        risk = 80
    elif predicted > 70:
        risk = 50
    else:
        risk = 20

    return {
        "predicted_demand": predicted,
        "risk": risk
    }
