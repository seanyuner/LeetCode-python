## [015 3Sum](https://leetcode.com/problems/3sum/description/)

**difficulty: medium**

**题目：**

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**examples：**

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

---
**solution：**
1. 此题虽然看起来和[001 TwoSum](https://github.com/seanyuner/LeetCode-python/tree/master/001%20Two%20Sum)有些类似，但是解法还是存在较大差异，解法也更丰富

2. 由于需要三个数字的和，O（n2）的复杂度是必须的

3. 前期可以将length不大于2的排除掉，也可以将列表正序便于处理

4. 具体解法：
  1. 排序后，遍历（遇到大于0直接break），从剩下的数中从两边往中间尝试，根据大小递减或递加，注意要跳过重复的
  2. 利用字典记录数值出现次数，先根据0情况来初始化，再区分正负数，分别排序后循环尝试，注意正负数相加结果的特点
  3. 先区分出有重复出现的数值并初始化为visited list，在从排序后的set中遍历，循环尝试并将尝试过的添加到visited list
