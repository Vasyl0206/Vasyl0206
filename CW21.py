def sorter(textbooks):
    #Cramming before a test can't be that bad?
    sort = sorted(textbooks, key = str.lower)
    return sort