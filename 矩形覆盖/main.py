def rectCover(number):
    if number==0:
        return 0
    if number==1:
        return 1
    if number==2:
        return 2
    k,a,b=2,1,2
    while(k<number):
        a,b=b,a+b
        k+=1
    return b