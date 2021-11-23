class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        res =0
        mod = 10**9 +7
        for i in range(1,n+1):
            c = len(bin(i))-2
            res = (res * (2**c) + i) %mod
        return res

re = Solution().concatenatedBinary(10000)
print(re)