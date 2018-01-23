# 45ms 74.99%
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = cmp(x, 0) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0


# 53ms 41.68%
class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        s = 0
        while x:
            s = s*10 + x%10
            x = x/10
        return sign*s if s < 2**31 else 0
