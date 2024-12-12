from functools import cache
import sys
sys.setrecursionlimit(10**4)
class Solution:
    def knightDialer(self, n: int) -> int:
        dir = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        mod = 10**9+7
        @cache
        def dfs(i,rest):
            if rest ==0:
                return 1
            res =0
            for a in dir[i]:
                if rest != 1 and a ==5:continue
                res += dfs(a,rest-1)
            return res %mod
        return sum([dfs(i,n-1) for i in range(10)]) %mod
    
re =Solution().knightDialer(3131)
print(re)