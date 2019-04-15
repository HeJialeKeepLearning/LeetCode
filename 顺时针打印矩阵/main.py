def printMatrix(matrix):
    if len(matrix) == 0:
        return
    col = len(matrix[0])
    row = len(matrix)
    if row != 1 and col != 1:
        index = 0
        while index < col:  # 打印最上面
            print(matrix[0][index])
            index += 1
        index = 1
        while index < row:  # 打印最右面一列
            print(matrix[index][col - 1])
            index += 1
        index = col - 2
        while index >= 0:  # 打印最下面一行
            print(matrix[row - 1][index])
            index -= 1
        index = row - 2
        while index > 0:  # 打印最左面一列
            print(matrix[index][0])
            index -= 1
        # 生成去掉外围一圈后的矩阵
        newmatrix = []
        indexrow = 1
        while indexrow < row - 1:
            newmatrix.append(matrix[indexrow][1:col - 1])
            indexrow += 1
        printMatrix(newmatrix)

    if row == 1:
        index = 0
        while index < col:
            print(matrix[0][index])
            index += 1
        return
    if col == 1:
        index = 0
        while index < row:
            print(matrix[index][0])
            index += 1
        return

printMatrix([[1],[2],[3],[4]])
