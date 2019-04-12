def ReverseList(pHead):
    plist = []
    p = pHead
    while p is not None:
        plist.append(p.val)
        p = p.next
    plist.reverse()
    p = pHead
    for i in plist:
        p.val = i
        p = p.next

    return pHead
