def jumpFloor(number):
    if number == 0:
        return 0
    k, a, b = 1, 1, 2
    while (k < number):
        a, b = b, a + b
        k += 1
    return a
