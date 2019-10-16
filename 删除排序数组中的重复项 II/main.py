class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        cnt = 0
        prev = nums[0]
        index = 0
        while index < length:
            if cnt <= 2:
                if nums[index] == prev:
                    cnt += 1
                else:
                    prev = nums[index]
                    cnt = 1
                index += 1
            else:
                index -= 1
                nums.pop(index)
                length -= 1
                cnt -= 1
        if cnt > 2:
            nums.pop()
        return length
