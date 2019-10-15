class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        target_row, target_col = 0, 0
        for target_row in range(len(matrix)):
            if matrix[target_row][0] >= target:
                break
        for target_col in range(len(matrix[0])):
            if matrix[0][target_col] >= target:
                break
        sub_matrix = [row[0:target_col + 1] for row in matrix[0:target_row + 1]]

        for each_row in sub_matrix:
            low, high = 0, len(each_row) - 1
            while low <= high:
                mid = (low + high) // 2
                if each_row[mid] > target:
                    high = mid - 1
                elif each_row[mid] < target:
                    low = mid + 1
                else:
                    return True
        return False
