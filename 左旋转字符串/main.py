def LeftRotateString(s, n):
    leftstr = s[:n]  # 左边n个字符串
    s = s[n:]
    return s+leftstr
