def PrintFromTopToBottom(root):
    if root is None:
        return []
    queue = []
    resultlist = []
    p = root
    queue.append(p)
    while len(queue)!=0:
        p = queue.pop(0)
        resultlist.append(p.val)
        if p.left is not None:
            queue.append(p.left)
        if p.right is not None:
            queue.append(p.right)

    return resultlist
