def search(keyword, knowledge):

    result = []

    for item in knowledge:

        if keyword.lower() in item["content"].lower():
            result.append(item)

    return result
