def FindNumbersWithSum(array, tsum):
    p = 0  # 从前向后的指针
    q = len(array) - 1  # 从后向前的指针
    while p <= q:
        sum = array[p] + array[q]
        if sum == tsum:
            return [array[p], array[q]]
        else:
            if sum > tsum:
                q -= 1
            else:
                p += 1
    return []

