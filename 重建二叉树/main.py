def reConstructBinaryTree(pre, tin):
    # write code here
    length = len(pre)
    if length == 0: # 终止条件
        return None
    root = TreeNode(pre[0])  # 记录根节点
    if root is not None:
        rootIndex = tin.index(root.val)  # 找到根节点在中序遍历中的索引index
        root.left = reConstructBinaryTree(pre[1:1 + rootIndex], tin[:rootIndex])
        root.right = reConstructBinaryTree(pre[rootIndex + 1:], tin[rootIndex + 1:])
    return root