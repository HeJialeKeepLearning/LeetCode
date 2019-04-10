def printListFromTailToHead(listNode):
    if listNode is None:
        return []
    p=listNode
    nodeList=[]
    nodeList.append(p.val)
    p=p.next
    while p is not None:
        nodeList.append(p.val)
        p=p.next

    nodeList.reverse()
    return nodeList