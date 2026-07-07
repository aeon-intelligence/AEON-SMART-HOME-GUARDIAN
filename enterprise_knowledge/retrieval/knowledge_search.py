def search_knowledge(records, keyword):

    results = []

    for item in records:

        if keyword.lower() in str(item).lower():
            results.append(item)

    return results
