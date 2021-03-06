# 题目
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
    s = "abc", t = "ahbgdc"
    
    返回 true.

示例 2:
    s = "axc", t = "ahbgdc"
    
    返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

# 解题思路
保存一个二维矩阵，对每个字母都检查和之前的字母是否相同，时间复杂度是o(len(s) * len(t))，空间复杂度也是o(len(s) * len(t))

改成使用回溯法，超出内存限制了，因为函数栈太深了。

因为是子序列，所以根本不用考虑中间插入了其他字母的影响，从前向后遍历t，对t的每个字母都保存当前匹配的最大长度，如果当前匹配：f(n) = f(n - 1) + 1，如果当前不匹配，f(n) = f(n - 1)

# 成绩
时间>69.55%
空间>20.17%
