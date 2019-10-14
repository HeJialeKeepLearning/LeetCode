class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row_index in range(length):
            for col_index in range(row_index + 1, length):
                matrix[row_index][col_index], matrix[col_index][row_index] = matrix[col_index][row_index], matrix[row_index][col_index]
        for each_row in matrix:
            each_row.reverse()
