def MoreThanHalfNum_Solution(numbers):
    cnt = {}
    for number in numbers:
        if number in cnt:
            numbercnt = cnt.get(number)
            cnt[number] = numbercnt + 1
        else:
            cnt[number] = 1
        if cnt.get(number) == int(len(numbers) / 2) + 1:
            return number
    return 0
