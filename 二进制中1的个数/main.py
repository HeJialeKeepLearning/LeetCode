def NumberOf1(n):
    if n<0:#负数flag=1
        flag=1
        n=-n
    else:#正数flag=0
        flag=0
    #对负数按位取反再+1
    if flag==1:
        n=n^0b11111111111111111111111111111111
        n+=1

    strx = bin(n)[2:]
    cnt = 0
    for c in strx:
        if c == '1':
            cnt += 1

    return cnt