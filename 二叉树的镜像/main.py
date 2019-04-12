def Mirror(root):

    if root is None:
        return root

    if root.left is not None or root.right is not None:  # 有子树
        root.left, root.right = root.right, root.left
    if root.left is not None:
        Mirror(root.left)
    if root.right is not None:
        Mirror(root.right)

    return root