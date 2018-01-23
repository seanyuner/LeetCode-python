# 1274ms 32.50%
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length  < 3:  return []
        
        nums = sorted(nums)
        res  = []
        for i in range(length - 2):
            if nums[i] > 0: break
            if (i > 0) and (nums[i] == nums[i-1]): continue
            
            l, r = i+1, len(nums) - 1
            oppo = -nums[i]
            while l < r:
                if nums[l] + nums[r] == oppo:
                    res.append([nums[i], nums[l], nums[r]])
                    while (l < r) and (nums[l] == nums[l+1]): l += 1
                    while (l < r) and (nums[r] == nums[r-1]): r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < oppo:
                    while (l < r) and (nums[l] == nums[l+1]): l += 1
                    l += 1
                else:
                    while (l < r) and (nums[r] == nums[r-1]): r -= 1
                    r -= 1
        return res


# 550ms 99.68%
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        if 0 in counter and counter[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        uniques = counter.keys()

        pos = sorted(p for p in uniques if p > 0)
        neg = sorted(n for n in uniques if n < 0)

        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in counter:
                    if n < inverse < p:
                        rst.append([n, inverse, p])
                    elif (inverse == p or inverse == n) and counter[inverse] > 1:
                        rst.append([n, inverse, p])
        return rst


# 757ms 98.65%
class Solution3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums.count(0) >= 3:
            result.append((0, 0, 0))
        seen = set()
        visited = set(x for x in nums if x in seen or seen.add(x))
        deduped = sorted(set(nums))
        for i, n in enumerate(deduped[:-1]):
            for n2 in deduped[i + 1:]:
                n3 = -(n2 + n)
                if n3 in visited and (n >= n3 or n3 == n2):
                    result.append([n, n2, n3])
            visited.add(n)
        return result
        
