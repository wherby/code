# Python 字符串比较速度很快？？
class Solution(object):
    def largestMerge(self, a, b):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res =""
        while a and b:
            if a>b:
                res +=a[0]
                a =a[1:]
            else:
                res +=b[0]
                b =b[1:]
        return res +a + b