import functools


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        @functools.lru_cache(None) 
        def dfs(n):
            if n <=1:
                return 1
            num = 0
            for i in range(1,n+1):
                left = dfs(i-1)
                right = dfs(n-i)
                #print(left,right,i)
                num += right *left
            return num
        return dfs(n)

re =Solution().numTrees(3)
print(re)