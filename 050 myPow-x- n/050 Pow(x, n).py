# 39ms 28.51%
class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n
   
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


# 37ms 50.03%
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n
   
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n = n / 2
        return res


# 35ms 61.24%
class Solution3(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1.0: return 1.0
        if n == 1: return x
        if n < 0: return 1 / self.myPow(x, -n)
        if n & 1: return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


# 37ms 50.03%
class Solution4(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1.0: return 1.0
        if n == 1: return x
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
