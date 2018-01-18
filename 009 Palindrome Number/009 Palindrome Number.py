# 208ms
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for i in range(int(len(x)/2)):
            if x[i] != x[-i-1]:
                return False
            else:
                pass
        return True


# 225ms
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return False if x < 0 else str(x) == str(x)[::-1]

    
# 335ms
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = x % 10 + reversed_num * 10
            x = x / 10
        return x == reversed_num or x == reversed_num / 10
