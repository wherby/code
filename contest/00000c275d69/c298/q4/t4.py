from functools import cache


class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """ 
        @cache
        def dfs(m,n):    
            mx =0
            for y,x,p in prices:
                if y<=m and x <=n:
                    ret = p + max(dfs(m,n-x) + dfs(m-y,x),dfs(m-y,n)+ dfs(y,n-x))
                    mx = max(mx,ret)
            return mx
        ret=  dfs(m,n)
        return ret

re = Solution().sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]])
print(re)