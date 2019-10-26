# 题目
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符
示例 1:

    输入: word1 = "horse", word2 = "ros"
    输出: 3
    解释: 
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
示例 2:

    输入: word1 = "intention", word2 = "execution"
    输出: 5
    解释: 
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')

# 解题思路
动态规划

状态：用dp[m][n]来表示word1前m个字符和word2前n个字符的编辑距离

转移方程：

    dp[m][n] = dp[m - 1][n - 1]     若word1[m] == word2[n]
    dp[m][n] = 1 + min(dp[m][n-1], dp[m-1][n], dp[m-1][n-1])      若word1[m] != word2[n]

初始化：相当于拿word1[0]匹配word2和拿word2[0]匹配word1的情况

状态转移方程的内涵：
1. 当dp[m][n] = 1 + dp[m][n-1]时，代表着通过给word2插入word1[m]的字符来追求相同
2. 当dp[m][n] = 1 + dp[m-1][n]时，代表着通过给word1插入word2[n]的字符来追求相同
3. 当dp[m][n] = 1 + dp[m-1][n-1]时，代表通过把word1[m]替换成word2[n]/word2[n]替换成word1[m]来追求相同

所以实际上写状态转移方程的时候，顾名思义，需要考虑当前的状态由之前的哪几种状态可以转换过来，不漏掉任何一种状态的方式，就是仔细根据转移方式来考虑。比如这道题，转移方式有删除、添加、替换，1和2都是添加，3对应的是替换。

时间复杂度、空间复杂度：o(len(word1) * len(word2))

# 总结
动态规划的困难题，也不是想象中那么难。。。还是得多做，多想。细节要注意：初始化、转移途径

# 成绩
时间>94.74%
空间>39.33%
