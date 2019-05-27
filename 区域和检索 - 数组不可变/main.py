class NumArray:
    listnum = []

    def __init__(self, nums):
        self.listnum = nums.copy()
        return

    def sumRange(self, i, j):
        return sum(self.listnum[i:j + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
