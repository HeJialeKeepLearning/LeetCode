## 解题思路
递归f(str)：若len(str)=1,直接return该数字对应的字母list,否则:f(str_withoutHeadChar)获取去掉头部数字的其余数字的字母序列，然后双重循环该序列和本层数字对应的字母序列
## 总结
1. python面向对象用的不太好，现在才算搞懂leetcode代码为什么有self参数
## 成绩
时间>46.63%