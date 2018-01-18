# 45ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                return [dict[num], i]
            dict[target - num] = i


# 36ms
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            dict[target - nums[i]] = i


# 5082ms
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return i, j
        return 'No two sum solution!'
