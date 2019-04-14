def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    # 获取needle首字母再haystack中的下标列表headlist
    c = needle[0]
    headlist = []
    for i in range(len(haystack)):
        if haystack[i] == c:
            headlist.append(i)
    # 按下标列表开始匹配
    for i in headlist:
        if haystack.find(needle, i, i + len(needle)) != -1:
            return i

    return -1
