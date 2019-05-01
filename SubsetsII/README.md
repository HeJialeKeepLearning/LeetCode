## 解题思路
与Subset相同，见[链接](https://github.com/HeJialeKeepLearning/OnlineJudge/tree/master/Subsets)
## 总结
和无重复的子集区别在于：
1. 判断的时候，增加一个判断：在已有子集上增加当前字母后的子集是否已经出现过
2. 因为这样的判断方式，会认为[1,4]和[4,1]是2个不同的子集，所以在开始选取子集之前先将list排序即可
## 成绩
时间>35.02%，空间>99.58%