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
1. 实现pow函数，即n个x的连乘
2. 首先可以处理特殊情况，a:n为0或者x为1；b:n为1；c：n为负
3. 大致有两种方案，一是循环n，二是循环但是调用函数自身，即self.myPow()，当指数为偶数时，将底数翻倍同时指数减半，从而达到逐渐降幂的效果
4. 有意思的是，实现**偶数判断**和**指数减半**时均有两种方法实现，也进行比较并发现了Python里较高效的方案，具体是**按位与1（&1）**优于**%2**，**/2** 优于**移位（>>1）**，具体对比可参见代码
