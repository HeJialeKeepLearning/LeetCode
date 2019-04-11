def Power(base, exponent):
    i = 1
    if exponent < 0:
        exponent = -exponent
        base = 1 / base
    list = [base]

    while pow(2, i) < exponent:
        base = pow(base, 2)
        list.append(base)
        i += 1
    list.reverse()
    bexStr = str(bin(exponent))[2:]
    result = float(1)
    index = 0
    for c in bexStr:
        if c == '1':
            result *= list[index]
        index += 1
    return result

Power(2, -3)
