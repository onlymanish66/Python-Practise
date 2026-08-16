def matchingStrings(stringList, queries):
    # Write your code here
    result = []
    for query in queries:
        a = stringList.count(query)
        result.append(a)
    return result