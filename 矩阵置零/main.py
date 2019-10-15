class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_cols = set()
        zero_flag = False
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] == 0:
                    zero_cols.add(col_index)
                    zero_flag = True
                if zero_flag and col_index == len(matrix[row_index]) - 1:
                    matrix[row_index] = [0] * len(matrix[row_index])
                    zero_flag = False
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index] and col_index in zero_cols:
                    matrix[row_index][col_index] = 0