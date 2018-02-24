## [050 myPow(x, n)](https://leetcode.com/problems/powx-n/description/)

** difficulty: medium**

**题目：**

Implement [pow(x, n)](http://www.cplusplus.com/reference/valarray/pow/).

**examples:**

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

---
***solution:*
1. 实现pow函数，即n个x的连乘
2. 大致有两种方案，一是循环n，二是循环但是调用函数自身，即self.myPow()
3. 首先可以处理特殊情况，a:n为0或者x为1；b:n为1；c：n为负
4. 对于两种循环，当指数为偶数时，将底数翻倍同时指数减半，从而达到逐渐降幂的效果
5. 有意思的是，实现偶数判断和指数减半时均有两种方法实现，也进行比较并发现了Python里较高效的方案，具体是* 按位与1（&1） *优于* &2 *，* /2 * 优于* 移位（>>1） *
