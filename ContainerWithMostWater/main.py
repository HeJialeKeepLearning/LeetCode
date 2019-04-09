def maxArea(height):
    p = 0
    q = len(height) - 1
    areaMax = 0
    while (p != q) & (p < q):
        if height[p] < height[q]:
            a = height[p]  # a是短的边长
            areaNew = a * (q - p)
            p += 1
        else:
            a = height[q]
            areaNew = a * (q - p)
            q -= 1
        if areaNew > areaMax:
            areaMax = areaNew

    return areaMax

maxArea([1, 2])
