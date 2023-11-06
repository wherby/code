class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        mx = max(a,b,c)
        res = a+b+c -mx
        return max(res,(mx+res)//2)