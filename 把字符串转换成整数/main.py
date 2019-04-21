def StrToInt(s):
    if len(s) == 0:
        return 0
    c = s[0]
    flag = True  # 正数
    if c == '+':
        s = s[1:]
    elif c == '-':
        flag = False  # 负数
        s = s[1:]
    if not s.isdigit():
        return 0
    snum = 0
    p = 0  # 每一位的权重
    index = len(s) - 1
    while index >= 0:
        snum = snum + (ord(s[index]) - ord('0')) * pow(10, p)
        index -= 1
        p += 1
    if flag:
        return snum
    else:
        return -snum
