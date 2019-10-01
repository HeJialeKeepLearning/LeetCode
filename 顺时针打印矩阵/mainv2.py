# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ret_list = []
        while matrix:
            ret_list.extend(matrix[0])
            matrix = self.turn_matrix(matrix)
        return ret_list

    def turn_matrix(self, matrix):
        ret_matrix = []
        col = len(matrix[0])
        row = len(matrix)
        for col_index in range(col):
            newline = []
            for row_index in range(1, row):
                newline.append(matrix[row_index][col_index])
            ret_matrix.append(newline)
        ret_matrix.reverse()
        return ret_matrix

Solution.printMatrix(Solution, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
