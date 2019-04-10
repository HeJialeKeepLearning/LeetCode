def removeDuplicates(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return
    pre = nums[0]
    index = 1
    while index < len(nums):
        p = nums[index]
        while pre == p:
            del nums[index]
            if index == len(nums):
                return
            p = nums[index]
        index += 1
        pre = p
    return
