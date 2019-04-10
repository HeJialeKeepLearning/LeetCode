def removeElement(nums, val):
    index = 0
    while index < len(nums):
        pval = nums[index]
        if pval == val:
            del nums[index]
        else:
            index += 1
    return
