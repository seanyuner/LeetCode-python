# 56ms 81.04%
class Solution1(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 首先找到倒数第一个逆序的元素
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 将找到的第一个逆序元素和倒数第一个大于该逆序元素的元素交换
        if i >= 0:
            j = length - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 交换位置后面元素倒序
        j = length - 1
        while i + 1 < j:
            nums[i + 1], nums[j] = nums[j], nums[i+1]
            i += 1
            j -= 1


# 55ms 87.64%
class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 首先找到倒数第一个逆序的元素
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 将找到的第一个逆序元素和倒数第一个大于该逆序元素的元素交换
        if i >= 0:
            j = length - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 交换位置后面元素倒序（没有逆序元素则返回数组反序）
        nums[i + 1:] = nums[i + 1:][::-1]
