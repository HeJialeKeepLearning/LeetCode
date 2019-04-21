def LastRemaining_Solution(n, m):
    if n == 0:
        return -1
    childlist = []
    index = 0  # 创建小孩的编号列表
    while index < n:
        childlist.append(index)
        index += 1
    delindex = 0
    while len(childlist) > 1:
        delindex = (delindex + m - 1) % len(childlist)
        del childlist[delindex]
    for v in childlist:
        if v != -1:
            return v
