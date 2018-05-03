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
1. 解法可以参考leetcode的[Solution](https://leetcode.com/problems/next-permutation/solution/)中的示意图，即下图，可以分为三步，一是逆序查找第一个倒序的元素，二是逆序查找第一个大于该倒序元素的元素，并交换，三是将第一个倒序元素后面的所有元素升序排列（直接[::-1]即可）。
<p align='center'> 
<img src=31_Next_Permutation.gif height=250> 
</p>

```
class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 逆序查找第一个倒序的元素
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 逆序查找第一个大于该倒序元素的元素，并交换
        if i >= 0:
            j = length - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 将第一个倒序元素后面的所有元素升序排列
        nums[i + 1:] = nums[i + 1:][::-1]
```

2. 如上述solution2所示，其实里面暗含了几种特殊情况
    2.1 一是如果数组是逆序的，如3,2,1，此时i<0接返回nums[::-1]
    2.2 二是如果找不到大于第一个逆序元素的元素，如1,3,2，此时第二步不会发生任何交换
