def isNumeric(s):
    dot = False  # 出现小数点
    eexit = False  # 出现e
    eindex = len(s) - 1  # 标记e出现的索引
    for si in range(len(s)):
        if ord(s[si]) > ord('9') or ord(s[si]) < ord('0'):  # 如果是特殊字符
            if s[si] == 'e' or s[si] == 'E':  # 如果特殊字符是e
                if eexit:  # 如果已经有e
                    return False
                else:  # 如果第一次出现e
                    eexit = True
                    eindex = si
                    if eindex == len(s) - 1:  # 如果e是最后一个字母
                        return False
            elif s[si] == '+' or s[si] == '-':  # 如果特殊字符是+/-
                if si == eindex + 1 or si == 0:  # 如果出现在e后或第1位
                    pass
                else:
                    return False
            elif s[si] == '.':  # 如果特殊字符是小数点
                if si <= eindex and not dot:  # 如果小数点出现在e之前，并且之前没出现过
                    dot = True  # 标记小数点已出现
                else:
                    return False
            else:
                return False

    return True
