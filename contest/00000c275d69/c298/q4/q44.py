from functools import cache


class Solution(object):
    def sellingWood(self, m, n, prices):
        dic =[[0]*(n+1) for _ in range(m+1)]
        for x,y,p in prices:
            dic[x][y] = p 
        @cache
        def dfs(h,w):
            ret = dic[h][w]
            
            for i in range(1,h//2+1):
                ret = max(ret,dfs(i,w)+dfs(h-i,w))
            for j in range(1,w//2 +1):
                ret = max(ret,dfs(h,j) + dfs(h,w-j))
            return ret
        return dfs(m,n)