# DP DFS Backtrack, bitmask
import math
from functools import lru_cache
class Solution:
    
    def minSessions(self, tasks, sessionTime) :
        n = len(tasks)

        @lru_cache(None)
        def dfs(mask):
            if mask ==0:
                return (1,0)
            ans = (math.inf,math.inf)
            for i in range(n):
                if mask &(1<<i):
                    pieces,last = dfs(mask- (1<<i))
                    full = (last + tasks[i] > sessionTime)
                    ans = min(ans, (pieces +full , tasks[i] +(1-full) *last ))
            return ans
        return dfs((1<<n)-1)[0]

tasks = [1,2,3]
re = Solution().minSessions(tasks,3)
print(re)
