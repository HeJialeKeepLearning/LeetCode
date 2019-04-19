def IsContinuous(numbers):
    if not numbers:
        return False
    numbers.sort()
    index = 0
    cnt = 0
    while index < len(numbers) - 1 and cnt >= 0:
        if numbers[index] == 0:
            cnt += 1
        else:
            if numbers[index] + 1 != numbers[index + 1]:
                cnt -= 1
                numbers.insert(index + 1, numbers[index] + 1)
        index += 1
    if cnt < 0:
        return False
    else:
        return True
