## 题目
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

## 解题思路
同样，使用辅助字典。异或的思路没想到，如果已知a^b，应该没办法直接分离出来a和b的吧……
## 注意点
需要根据a^b的某个不为0的位数，将数组分成2部分，放弃了
## 成绩
时间>85.17%，空间>5.34%
