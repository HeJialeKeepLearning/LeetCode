def duplicate(numbers, duplication):
    aux = [0] * len(numbers)
    for v in numbers:  # 初始化辅助列表
        if aux[v] == 1:
            aux[v] += 1
        else:
            aux[v] = 1
    for index, v in enumerate(aux):
        if v > 1:
            duplication[0] = index
            return True
    return False
