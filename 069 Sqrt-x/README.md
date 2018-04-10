## [069 Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)

**difficulty: easy**

**题目：**

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

**examples:**

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

---
**solution:**
1. **二分查找**。设置左右界，根据二者大小关系判断循环是否结束
2. 每次计算平均值（平均值和x/平均值， 初始化为x/2），根据平均值平方与x大小关系判断循环是否结束
