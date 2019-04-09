def mergeTwoLists(l1, l2):
    p = l1
    q = l2

    if (p is None) | (q is None):
        if p is None:
            if q is None:#如果p和q均为空
                return []
            else:#p空q不空
                return q
        else:#q空p不空
            return p

    if p.val < q.val:
        initx = p.val
        p = p.next
    else:
        initx = q.val
        q = q.next

    mergeList = ListNode(initx)#初始化一个的节点
    mergeListHead = mergeList
    while (p != None) & (q != None):
        mergeList.next = ListNode(0)
        mergeList = mergeList.next
        if p.val < q.val:
            mergeList.val=p.val
            p = p.next
        else:
            mergeList.val = q.val
            q = q.next
    while p != None:
        mergeList.next = ListNode(0)
        mergeList = mergeList.next
        mergeList.val = p.val
        p = p.next
    while q != None:
        mergeList.next = ListNode(0)
        mergeList = mergeList.next
        mergeList.val = q.val
        q = q.next
    return mergeListHead
