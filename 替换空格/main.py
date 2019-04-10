def replaceSpace(s):
    newStr=""
    for c in s:
        if c==' ':
            newStr+='%20'
        else:
            newStr+=c
    return newStr