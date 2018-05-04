## [046 Permutaions](https://leetcode.com/problems/permutations/description/)

**difficulty: medium**

**题目：**

Given a collection of distinct integers, return all possible permutations.

**examples:**

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

---
**solution:**

1. 显然这道题目可以利用递归，从n个元素的数组一直分解到1个元素，将每个元素插入到剩下元素构成所有不同排列的首位，如解法1所示。

2. 同样是递归，将数组的首个元素插入到剩下所有元素构成的所有排列的不同位置即可，如解法2所示。

3. 元素个数递增地构建当前所有元素能组成的排列，对于新的元素，插入已有排列不同位置则得到不同新的排列，直到所有元素插入完即可，如解法3所示。

4. python有自带的itertools函数进行排列组合，效率也是非常高。
