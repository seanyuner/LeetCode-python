# 58ms 77.18%
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        mid = x / 2
        while mid ** 2 > x:
            mid = (mid + x / mid) / 2
        return mid
 

# 53s 93.39%
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        
        start = 0
        end = x
        mid = (start + end) / 2
        while mid:
            if mid ** 2 > x:
                end = mid
            else:
                start = mid
            last_mid = mid
            mid = (start + end) / 2
            if mid == last_mid:
                break
                
        return mid


# 63ms 54.31%
class Solution3(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        start, end = 1, x / 2
        while start < end:
            mid = (start + end + 1) / 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid -1
        return end

    
# 63ms 54.31%
class Solution4(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        start = 1
        end = x
        while(start <= end):
            mid = start + (end - start) / 2
            sqrt = x / mid
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                end = mid - 1
            else:
                start = mid + 1
        return end
