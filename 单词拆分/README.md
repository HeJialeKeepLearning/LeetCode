# 题目
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。
示例 3：

    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

# 解题思路
别人的思路

动态规划，状态dp[i]表示s中前i的字符是否在字典中

转移方程：

    dp[i] = (dp[j] and s[j:i] in dict)
也就是说，如果dp[j] = True，说明s[0:j+1]都在字典中，此时只需要看s[j:i]是否在字典中即可

初始化：dp = [False]

# 成绩
时间>88.80%
空间>25.75%
