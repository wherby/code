from functools import cache
from itertools import pairwise
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        availble = []
        for i in range(3**m):
            ls=[]
            cur = i
            for _ in range(m):
                ls.append(cur%3)
                cur = cur //3 
            isG = True
            for a,b in pairwise(ls):
                if a ==b:
                    isG =False
            if isG:
                availble.append(i)
        @cache
        def isGood(x,y):
            curx,cury = x,y
            for _ in range(m):
                if curx%3 == cury%3:
                    return False
                curx = curx//3
                cury = cury //3
            return True
        @cache
        def dfs(i,state):
            if i == n:
                return 1 
            ret = 0
            for ns in availble:
                if isGood(state,ns):
                    ret +=dfs(i+1,ns)
            return ret%mod
        mod = 10**9+7 
        ret = 0
        for st in availble:
            ret += dfs(1,st)
        return ret %mod

re = Solution().colorTheGrid(5,5)
print(re)
