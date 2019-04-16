def FindGreatestSumOfSubArray(array):
    max = array[0]
    cnt = array[0]
    for i in array[1:]:
        if cnt > 0:
            cnt += i
        else:
            cnt = i
        if max < cnt:
            max = cnt
    return max
