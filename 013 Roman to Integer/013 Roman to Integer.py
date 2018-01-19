# 123ms 81.1%
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res = 0
        last_val = 0
        for char in s:
            val = roman[char]
            if last_val in [1, 10, 100]:
                if val > last_val:
                    res -= 2* last_val
            res += val
            last_val = val
        return res


# 145ms 44.6%
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num = 0
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i+1]]:
                num += roman[s[i]]
            else:
                num -= roman[s[i]]
        return num+roman[s[-1]]
