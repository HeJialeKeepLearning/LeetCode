class Solution:
    def compress(self, chars):
        pre = None
        cnt = 0
        edit_index = 0
        for index in range(len(chars)):
            if not pre:
                pre = chars[index]
                cnt = 0
            if pre != chars[index]:
                chars[edit_index] = pre
                edit_index += 1
                if cnt > 1:
                    cnt_list = list(str(cnt))
                    length = len(cnt_list)
                    chars[edit_index: edit_index + length] = cnt_list
                    edit_index += length
                pre = chars[index]
                cnt = 0
            cnt += 1
        chars[edit_index] = pre
        edit_index += 1
        if cnt > 1:
            cnt_list = list(str(cnt))
            length = len(cnt_list)
            chars[edit_index: edit_index + length] = cnt_list
            edit_index += length
        return edit_index
