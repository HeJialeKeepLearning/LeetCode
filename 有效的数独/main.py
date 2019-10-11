class Solution:
    def isValidSudoku(self, board):
        length = len(board)
        # check 3*3
        for row_index in range(0, length, 3):
            row_span = board[row_index:row_index + 3]
            for col_index in range(0, length, 3):
                small_borad = []
                small_borad.extend([col_span[col_index:col_index + 3] for col_span in row_span])
                if not self.is_validate_small(small_borad):
                    return False
        # check row & col
        num_dict = {}
        for row in board:
            row_dict = {}
            for col in row:
                if col == '.':
                    continue
                if col in row_dict:
                    return False
                row_dict[col] = 1
                num_list = num_dict.get(col, [])
                if not num_list:
                    num_dict[col] = [row.index(col)]
                    continue
                col_index = row.index(col)
                if col_index in num_list:
                    return False
                num_list.append(col_index)
        return True

    def is_validate_small(self, board):
        num_dict = {}
        for row in board:
            for col in row:
                if col != '.':
                    if col in num_dict:
                        return False
                    num_dict[col] = 1
        return True
