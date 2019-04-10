def Find(target, array):
    # write code here
    if len(array) == 1:
        return False
    for i in range(len(array)):
        arrayLine = array[i]
        maxLine = max(arrayLine)
        minLine = min(arrayLine)
        if target >= minLine and target <= maxLine:
            for j in range(len(arrayLine)):
                if target == arrayLine[j]:
                    return True
    return False
