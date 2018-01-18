## [007 reverse integer](https://leetcode.com/problems/reverse-integer/description/)

difficulty:easy

**题目:**

Given a 32-bit signed integer, reverse digits of an integer.


**示例:**

Input: 123
Output:  321

Input: -123
Output: -321


**Note:**

Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


**solution:**
1. 首先可以将abs小于10的直接返回
2. 判断正负，可以数值比较，也可以str(x)[0]
3. 翻转，可以str(x)[::-1]，也可以循环使用%/
4. 判断溢出，x.bit_length() < 32 或者 abs(x) < 2 ** 31 或者 abs(x) <= 0x7FFFFFFF(=2147483647=2^31-1)
