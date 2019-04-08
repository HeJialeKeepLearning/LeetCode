def romanToInt(s):
    romanNum={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    #对特殊情况(str只有1位)进行处理
    if len(s)==1:
        return romanNum[s]

    num=0
    i=1
    while i<=len(s):
        if i==len(s):
            num=num+romanNum[s[i-1]]
            break
        c=s[i]
        cPre=s[i-1]
        if romanNum[cPre]>=romanNum[c]:
            num=num+romanNum[cPre]
        else:
            num=num-romanNum[cPre]+romanNum[c]
            i+=1
        i+=1

    return num

print(romanToInt('III'))