def isValid(s: str) -> bool:
    if(len(s)==0):
        return True
    stack = [s[0]]
    stackLen=1
    pun2num = {'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3, }
    for i in range(1, len(s)):
        stack.append(s[i])
        stackLen+=1
        punPre = stack[stackLen-2]#栈顶元素的前一个元素
        punP = stack[stackLen-1]#栈顶元素
        if pun2num[punPre] + pun2num[punP] == 0:
            stack.pop()
            stack.pop()
            stackLen-=2

    if stackLen == 0:
        return True
    else:
        return False

print(isValid('()[]{}'))
