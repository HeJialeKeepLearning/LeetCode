def intToRoman(num):
    roman1=['I','II','III','IV','V','VI','VII','VIII','IX']#1~9
    roman2=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']#10~90
    roman3=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']#100~900
    roman4=['M','MM','MMM']#1000~3000
    roman=[roman1,roman2,roman3,roman4]

    romanlist=[]
    digit=0#计算输入的数字有几位
    numTemp=num
    while(numTemp>=1):
        digit+=1
        numTemp/=10

    index=digit-1
    while(int(num)>0):
        digitNumber=int(num/(10**index))
        if (digitNumber == 0):
            index -= 1
            continue
        romanlist.append(roman[index][digitNumber-1])
        num=num%(10**index)
        index-=1

    return "".join(romanlist)
