class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda sub_list: sub_list[0])
        merged_list = []
        begin, end = intervals[0]
        for each_interval in intervals[1:]:
            new_begin, new_end = each_interval
            if new_begin <= end:
                if end < new_end:
                    end = new_end
            else:
                merged_list.append([begin, end])
                begin, end = new_begin, new_end
        merged_list.append([begin, end])
        return merged_list

