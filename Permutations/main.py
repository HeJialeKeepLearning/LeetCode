def permute(nums):
    if not nums:
        return [[]]
    if len(nums) == 1:
        return [nums]
    resultlist = []
    for c in nums:
        crest = [x for x in nums if x != c]
        nextlists = permute(crest)
        for nextlist in nextlists:
            currentlist=[c]
            for nexte in nextlist:
                currentlist.append(nexte)
            resultlist.append(currentlist)
    return resultlist

permute([1,2,3])