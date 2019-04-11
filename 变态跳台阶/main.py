def jumpFloorII(number):
    def jumpFloor(number):
        list = [1]
        if number == 1:
            return list[0]
        else:
            for k in range(1, number):
                e = 1  # 本级台阶的方法数
                for ek in range(k):
                    e += list[ek]
                list.append(e)
        return list[number - 1]
