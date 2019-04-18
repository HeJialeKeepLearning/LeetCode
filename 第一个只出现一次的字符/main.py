def FirstNotRepeatingChar(s):
    chardict = {}
    for c in s:
        if c in chardict:
            chardict[c] += 1
        else:
            chardict[c] = 1
    index = len(s) - 1
    for key, value in chardict.items():
        if value == 1:
            nowindex = s.index(key)
            if index > nowindex:
                index = nowindex

    return index
