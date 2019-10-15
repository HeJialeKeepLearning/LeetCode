class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            head, tail = row[0], row[-1]
            if head <= target <= tail:
                low, high = 0, len(row) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if target > row[mid]:
                        low = mid + 1
                    elif target < row[mid]:
                        high = mid - 1
                    else:
                        return True
                return False
        return False