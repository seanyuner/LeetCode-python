## [031 Next Permutaion](https://leetcode.com/problems/next-permutation/)

**difficulty: medium**

**题目：**

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

**examples:**

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

---
**solution:**
1. **二分查找**。设置左右界，根据二者大小关系判断循环是否结束
2. 每次计算平均值（平均值和x/平均值， 初始化为x/2），根据平均值平方与x大小关系判断循环是否结束
