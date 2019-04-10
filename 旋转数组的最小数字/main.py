def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    if len(rotateArray) == 1:
        return rotateArray[0]
    for i in range(1, len(rotateArray)):
        if rotateArray[i] < rotateArray[i - 1]:
            return rotateArray[i]
