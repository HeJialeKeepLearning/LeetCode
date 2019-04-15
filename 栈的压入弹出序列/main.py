def IsPopOrder(pushV, popV):
    check = [val for val in pushV if val not in popV]
    if len(check) != 0:  # 如果压入序列和弹出序列有不一致的元素
        return False
    pushVindex = 0
    while pushVindex < len(pushV):
        x = pushV[pushVindex]
        prelist = pushV[:pushVindex]  # prelist为压入序列中x之前的元素序列
        popVindex = 0  # 从0开始寻找x出现在弹出序列中的下标
        popxIndex = []  # 记录x出现在弹出序列中的下标
        while popVindex < len(popV):
            if x == popV[popVindex]:
                popxIndex.append(popVindex)
            popVindex += 1
        for popVxindex in popxIndex:  # 对弹出序列中每一个可能的x
            poplist = popV[popVxindex + 1:]  # poplist为弹出序列中x之后的元素序列
            # 获取poplist和prelist的交集
            popjiao = [val for val in poplist if val in prelist]
            prejiao = [val for val in prelist if val in poplist]
            prejiao.reverse()
            if prejiao != popjiao:
                return False
        pushVindex += 1
    return True

IsPopOrder([1], [2])
