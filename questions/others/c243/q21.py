class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        m = len(n)
        if n[0] != "-":
            for i in range(m):
                if int(n[i]) <x:
                    return n[:i] + str(x) + n[i:]
        else:
            for i in range(1,m):
                if int(n[i])>x:
                    return n[:i]+str(x) + n[i:]
        return n +str(x)

re = Solution().maxValue(n = "-132", x = 3)
print(re)