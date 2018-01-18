
## [009 Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

**题目:**

Determine whether an integer is a palindrome. Do this without extra space.


**hints:**

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


**solution:**
1. 由于负数不是回文数，可首先直接判断并返回false
2. 正数中10的倍数也不是回文数，可先返回false
3. 剩下的和[007](https://github.com/seanyuner/LeetCode-python/tree/master/007%20Reverse%20Integer)就有些类似了，可以使用str(),也可以使用循环%/
4. 若使用str()，理论上不必先处理负数，*return str(x) == str(x)[::-1]* 一行即可
5. 注意奇位数和偶位数会不会有影响
