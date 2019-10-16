class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word = list(word)

        def backtrace(cur_index, cur_list, history_path):
            if not cur_list:
                return
            if cur_index == len(word) - 1:
                output.pop()
                return
            for cur_pos in cur_list:
                history_path.append(cur_pos)
                next_list = []
                next_word = word[cur_index + 1]
                x, y = cur_pos
                for new_pos in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if new_pos in history_path:
                        continue
                    new_x, new_y = new_pos
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                        if board[new_x][new_y] == next_word:
                            next_list.append([new_x, new_y])
                backtrace(cur_index + 1, next_list, history_path)
                if not output:
                    return
                history_path.pop()

        output = [False]
        first_pos = []
        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                if board[row_index][col_index] == word[0]:
                    first_pos.append([row_index, col_index])
        backtrace(0, first_pos, [])
        return output == []
