# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) <= 1:
            return True
        root = sequence.pop()
        left_sequence = []
        right_sequence = []
        subtree_null = True
        for element in sequence:
            if element > root:
                subtree_null = False
                break
        last_left_index = sequence.index(element)
        if subtree_null:
            last_left_index += 1
        left_sequence.extend(sequence[:last_left_index])
        right_sequence.extend(sequence[last_left_index:])

        for left_e in left_sequence:
            if left_e > root:
                return False
        for right_e in right_sequence:
            if right_e < root:
                return False
        if not left_sequence:
            left_sequence.append(None)
        if not right_sequence:
            right_sequence.append(None)
        return self.VerifySquenceOfBST(left_sequence) & self.VerifySquenceOfBST(right_sequence)

s = Solution()
s.VerifySquenceOfBST([4, 6, 7, 5])
