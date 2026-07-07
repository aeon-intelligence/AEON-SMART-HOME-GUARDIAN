def match_agent(task, agents):

    for agent in agents:

        if agent["capability"] == task:
            return agent

    return None
