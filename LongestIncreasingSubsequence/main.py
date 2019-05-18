class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        f = [1]
        i = 1
        while i < len(nums):
            j = 0
            maxlen = 1
            while j < i:
                if nums[i] > nums[j]:
                    if f[j] + 1 > maxlen:
                        maxlen = f[j] + 1
                j += 1
            f.append(maxlen)
            i += 1
        return max(f)
