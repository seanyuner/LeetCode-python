## [001 Two Sum](https://leetcode.com/problems/two-sum/description/)

**difficulty:easy**

**题目：**

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


**examples：**

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


**solution:**
1. 配对问题
2. 建立dict存储，key为目标值，value为当前值index，循环出现key，则返回两个index即可
3. 循环可以用range(len(x))，也可以使用enumerate(x)
4. 也可使用类似冒泡法，但是time complicity 为 O(n^2)
