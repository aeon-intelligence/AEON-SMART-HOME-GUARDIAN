def evaluate(agent, completed, accuracy):

    score = (
        completed * 0.5
        +
        accuracy * 0.5
    )

    return {
        "agent": agent,
        "performance_score": score
    }
