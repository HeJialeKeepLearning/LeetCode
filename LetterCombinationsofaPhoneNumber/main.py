number2letter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

def letterCombinations(digits):
    if len(digits) == 0: return []
    if len(digits) == 1:
        return number2letter[digits]
    else:
        digitWithoutHead = digits[1:]  # 去掉该字符串的头
        digitHead = digits[0]  # 字符串头
        nextList = letterCombinations(digitWithoutHead)
        letterList = []
        for c in number2letter[digitHead]:
            for i in range(len(nextList)):
                letterList.append(c + nextList[i])
    return letterList

print(letterCombinations("23"))
