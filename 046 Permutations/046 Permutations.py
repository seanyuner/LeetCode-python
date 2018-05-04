# 79ms 30.04%
class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#        if not nums:
 #           return [[]]
  #      return [[nums[i]] + j for i in range(len(nums)) \
   #             for j in self.permute(nums[:i] + nums[i + 1:])]
    
        return [[nums[i]] + j for i in range(len(nums)) for j in self.permute(nums[:i] + nums[i + 1:])] or [[]]


# 67ms 89.55%
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums] if len(nums) == 1 else []
        else:
            res = []
            for p in self.permute(nums[1:]):
                for i in range(len(p) + 1):
                    res.append(p[:i] + [nums[0]] + p[i:])
            return res


# 62ms 98.82%
class Solution3(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_res.append(perm[:i] + [num] + perm[i:])
            res = new_res
        return res


# 70ms 75.93%
class Solution4(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        
        stack=[[[nums[0]], 0]]
        i = 0
        res = []
        
        while(stack):
            arr, index = stack.pop()
            if index == len(nums) - 1:
                res.append(arr)
            else:
                for i in range(len(arr) + 1):
                    newPermutation = arr[:i] + [nums[index + 1]] + arr[i:]
                    stack.append([newPermutation, index + 1])
        return res


# 60ms 99.75%
# import itertools # python3需要import
class Solution5(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums, len(nums)))
