# -*- coding:utf-8 -*-
import copy

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        # 从给定的列表得到矩阵mat
        mat = [matrix[i * cols:i * cols + cols] for i in range(rows)]
        cnt = 0  # 记录path的首字母出现次数
        for row in mat:
            cnt += row.count(path[0])
        if cnt == 0:  # 第一个字母不在矩阵中
            return False
        sig = [[0 for i in range(cols)] for j in range(rows)]  # 记录是否已经走过，1是已经采用，2是不适合作为开头
        bomzone = [[0 for i in range(4)] for j in range(len(path))]  # 记录每个点周围的4个雷区，0上，1右，2下，3左
        stack = [path[0]]  # 存放当前找到的路径
        # 第一次运行，先把首字母放进去
        for i in range(rows):
            flag = False
            for j in range(cols):
                if mat[i][j] == path[0]:
                    sig[i][j] = 1
                    flag = True
                    break
            if flag:
                break
        index = 1
        if index == len(path):
            return True
        dir = []  # 记录本次选择了上下左右哪个方向，0上，1右，2下，3左
        while stack:  # 只要栈不空，就一直循环下去
            c = path[index]
            if i + 1 < rows and sig[i + 1][j] != 1 and mat[i + 1][j] == c and bomzone[index][2] == 0:
                i += 1
                sig[i][j] = 1
                stack.append(c)
                index += 1
                dir.append(2)
            elif i - 1 >= 0 and sig[i - 1][j] != 1 and mat[i - 1][j] == c and bomzone[index][0] == 0:
                i -= 1
                sig[i][j] = 1
                stack.append(c)
                index += 1
                dir.append(0)
            elif j + 1 < cols and sig[i][j + 1] != 1 and mat[i][j + 1] == c and bomzone[index][1] == 0:
                j += 1
                sig[i][j] = 1
                stack.append(c)
                index += 1
                dir.append(1)
            elif j - 1 >= 0 and sig[i][j - 1] != 1 and mat[i][j - 1] == c and bomzone[index][3] == 0:
                j -= 1
                sig[i][j] = 1
                stack.append(c)
                index += 1
                dir.append(3)
            else:  # 如果四周都没有找到
                if len(stack) == 1:  # 如果已经退到第一个字母了
                    cnt -= 1  # 第一个字母在矩阵中的出现次数-1
                    if cnt == 0:  # 如果第一个字母已经没了
                        stack.pop()  # 退栈，此时应该是空栈，返回False
                        return False
                    else:  # 如果还有第一个字母
                        sig[i][j] = 2  # 更换首字母位置，并且禁止该位置作为首字母
                        while i < rows:
                            flag = False
                            j = 0
                            while j < cols:
                                if sig[i][j] == 0 and mat[i][j] == path[0]:
                                    sig[i][j] = 1
                                    flag = True
                                    break
                                j += 1
                            if flag:
                                break
                            i += 1
                        index = 1
                else:  # 如果是第一个字母后的字母找不到，退栈，复位
                    stack.pop()
                    sig[i][j] = 0
                    if not stack:  # 如果退成空栈了
                        return False
                    index -= 1
                    dirtmp = dir.pop()
                    bomzone[index][dirtmp] = 1  # 此方向不要再走了
                    # 指针复位
                    if dirtmp == 0:
                        i += 1
                    elif dirtmp == 1:
                        j -= 1
                    elif dirtmp == 2:
                        i -= 1
                    elif dirtmp == 3:
                        j += 1
            if index == len(path):
                return True
