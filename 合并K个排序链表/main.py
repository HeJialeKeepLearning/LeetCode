# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        candidates = [head for head in lists if head]
        candidates.sort(key = lambda x: x.val)
        init_head = ListNode(-1)
        p = init_head
        while candidates:
            cur_min = candidates.pop(0)
            p.next = cur_min
            p = cur_min
            to_insert = cur_min.next
            if not to_insert:
                continue
            low, high = 0, len(candidates) - 1
            while low <= high:
                mid = (low + high) // 2
                if candidates[mid].val < to_insert.val:
                    low = mid + 1
                elif candidates[mid].val > to_insert.val:
                    high = mid - 1
                else:
                    candidates.insert(mid, to_insert)
                    break
            if low > high:
                candidates.insert(low, to_insert)
        return init_head.next
