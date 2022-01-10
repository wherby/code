# https://leetcode-cn.com/contest/weekly-contest-256/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
# use DFS only will timeout qiestion 

```
import functools
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        mx = n
        tasks.sort()
        validState = []
        
        @functools.lru_cache(None) 
        def verify(subSet):
            cnt =0
            for i in range(n):
                if 1<<i & subSet >0:
                    cnt += tasks[i]
            return cnt <= sessionTime
        for i in range(1,1<<n):
            if verify(i):
                validState.append(i)
        #print(validState)
        @functools.lru_cache(None) 
        def dfs(state,cnt):
            nonlocal mx
            if cnt > mx:
                return
            if state ==0:
                mx = min(mx,cnt)
            for va in validState:
                if va &state == va:
                    dfs(state-va, cnt+1)
        dfs((1<<n)-1,0)
        return mx
```


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
                if mask &(1<<i):   #遍历了所有可能的组合 
                    pieces,last = dfs(mask- (1<<i))
                    full = (last + tasks[i] > sessionTime)
                    ans = min(ans, (pieces +full , tasks[i] +(1-full) *last ))
            return ans
        return dfs((1<<n)-1)[0]

## 用backtrack 的方式把每个状态的最小值求出。小猫坐缆车题目
## 回溯法 algorithm/basic/basic.md