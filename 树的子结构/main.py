def HasSubtree(pRoot1, pRoot2):
    if pRoot1 is None or pRoot2 is None:
        return False
    def firstvisit(root):
        visitlist = ''
        visitlist += str(root.val)
        if root.left is not None:
            visitlist += firstvisit(root.left)
        if root.right is not None:
            visitlist += firstvisit(root.right)
        return visitlist

    pfirstlist1 = firstvisit(pRoot1)
    pfirstlist2 = firstvisit(pRoot2)

    if pfirstlist2 in pfirstlist1:
        return True
    else:
        return False