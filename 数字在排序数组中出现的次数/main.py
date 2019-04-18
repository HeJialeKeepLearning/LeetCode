def GetNumberOfK(data, k):
    try:
        kindex = data.index(k)
        cnt = 1
        for i in range(kindex + 1, len(data)):
            if data[i] == k:
                cnt += 1
        return cnt
    except ValueError:
        return 0
