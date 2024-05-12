class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(i):
            if i ==0:
                return 0 
            if i==1:
                return 1
            ret = i 
            ret = min(ret, i%2 + dfs(i//2)+1)
            ret = min(ret,i%3 +dfs(i//3)+1)
            return ret
        return dfs(n)