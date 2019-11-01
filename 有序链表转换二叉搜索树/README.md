# 题目
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

    示例:
    
    给定的有序链表： [-10, -3, 0, 5, 9],
    
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
    
          0
         / \
       -3   9
       /   /
     -10  5

# 解题思路
这道题和有序列表转换为二叉搜索树很相似，就是列表换成了链表。所以无脑版的思路就是，遍历一次链表，把数值保存在列表里，再左右递归。更好的思路是，其实我们发现，每次我们重点在于需要找到中间的那个节点，所以如果能找到链表中间的节点，就不用保存到列表里了，这道题就变成了先找链表中间节点，再左右递归喽。

时间复杂度o(n)
# 成绩
时间>87.61%
空间>74.83%
# 代码
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        slow, fast = head, head
        pre_slow = head
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        pre_slow.next = None
        if slow != fast:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
        return root

```